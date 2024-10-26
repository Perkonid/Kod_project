from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Импортируем для сообщений
from .models import CustomUser
from .forms import UserForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Organization
from django.contrib.auth.decorators import user_passes_test
from .forms import OrganizationForm  # Импортируем OrganizationForm
from django.shortcuts import render


@login_required
def work_view(request):
    query = request.GET.get('q', '').lower()
    organizations = Organization.objects.all()
    if query:
        organizations = organizations.filter(name__isnull=False)
        organizations = [org for org in organizations if query in org.name.lower()]
    organizations = sorted(organizations, key=lambda x: x.name)
    return render(request, 'users/work.html', {'organizations': organizations, 'query': query})



@login_required  # Доступ только для залогинившихся пользователей
def delete_user(request, user_id):
    if not request.user.is_superuser:  # Проверка на суперпользователя
        messages.error(request, "У вас нет доступа к этой операции.")
        return redirect('admin:index')  # Перенаправление на админку

    user_to_delete = get_object_or_404(CustomUser, id=user_id)  # Получаем пользователя по ID
    user_to_delete.delete()  # Удаляем пользователя
    messages.success(request, "Пользователь успешно удален.")  # Сообщение об успешном удалении
    return redirect('team')  # Перенаправляем на страницу team


@login_required  # Доступ только для залогинившихся пользователей
def team_view(request):
    if not request.user.is_superuser:  # Проверяем, является ли пользователь суперпользователем
        messages.error(request, "У вас нет доступа к этой странице.")  # Сообщение об ошибке
        return redirect('admin:index')  # Перенаправляем на админку или другую страницу

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Не сохраняем сразу
            user.set_password(form.cleaned_data['password'])  # Устанавливаем пароль
            form.save()
            return redirect('team')  # Перенаправляем на страницу team после добавления

    users = CustomUser.objects.all()  # Получаем всех пользователей
    form = UserForm()  # Создаем пустую форму

    return render(request, 'users/team.html', {'users': users, 'form': form})  # Отправляем данные в шаблон


# Представление для логина
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # Аутентификация пользователя

        if user is not None:
            login(request, user)  # Логин пользователя
            if user.is_superuser:  # Проверяем, является ли пользователь суперпользователем
                return redirect('team')  # Перенаправляем на страницу team
            else:
                return redirect('work')  # Перенаправляем на страницу work для обычных пользователей
        else:
            messages.error(request, "Неверные имя пользователя или пароль.")  # Ошибка при логине

    return render(request, 'users/login.html')  # Отправляем на страницу логина


@login_required
def detalization_view(request, org_id):
    # Получаем полные данные по конкретной организации
    organization = get_object_or_404(Organization, id=org_id)
    return render(request, 'users/detalization.html', {'organization': organization})


# Всё, что касаемо организаций
# Проверка на суперпользователя
def is_superuser(user):
    return user.is_authenticated and user.role == 'superuser'


# Проверка на администратора
def is_admin(user):
    return user.is_authenticated and user.role in ['admin', 'superuser']


# Проверка на обычного пользователя
def is_user(user):
    return user.is_authenticated and user.role == 'user'


# Проверка на роль админа или суперпользователя
def is_admin_or_superuser(user):
    return user.is_superuser or user.role == 'admin'


# Страница для создания и удаления организаций (доступна только суперпользователю)
@user_passes_test(is_admin_or_superuser)
@login_required
def create_organization(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Организация успешно добавлена.")
            return redirect('work')  # Перенаправляем на work после создания организации
    else:
        form = OrganizationForm()

    return render(request, 'users/create_organization.html', {'form': form})


# Функция для редактирования организаций (админ и суперпользователь)
@user_passes_test(is_admin)
@login_required
def edit_organization(request, org_id):
    organization = get_object_or_404(Organization, id=org_id)
    if request.method == 'POST':
        form = OrganizationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            messages.success(request, "Организация успешно обновлена.")
            return redirect('work')
    else:
        form = OrganizationForm(instance=organization)
    return render(request, 'users/edit_organization.html', {'form': form, 'organization': organization})


# Удаление организации (только для суперпользователя)
@user_passes_test(is_superuser)
@login_required
def delete_organization(request, org_id):
    organization = get_object_or_404(Organization, id=org_id)
    organization.delete()
    messages.success(request, "Организация успешно удалена.")
    return redirect('work')

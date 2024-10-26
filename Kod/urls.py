from django.contrib import admin
from django.urls import path
from users import views  # Импортируем представления из приложения users
from django.contrib.auth.views import LogoutView  # Импортируем LogoutView
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('team/', views.team_view, name='team'),  # URL для страницы team
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),  # URL для удаления пользователей
    path('', views.login_view, name='login'),  # URL для страницы логина
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  # URL для выхода с редиректом на страницу логина
    path('work/', user_views.work_view, name='work'), # URL для страницы work
    path('detalization/<int:org_id>/', user_views.detalization_view, name='detalization'),
    path('create_organization/', user_views.create_organization, name='create_organization'),
    path('edit_organization/<int:org_id>/', user_views.edit_organization, name='edit_organization'),
    path('delete_organization/<int:org_id>/', user_views.delete_organization, name='delete_organization'),
]



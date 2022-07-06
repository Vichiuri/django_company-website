from django.contrib.auth.views import LogoutView
from django.urls import path

from tally.users import views
from tally.users.auth.login import login

app_name = "users"
urlpatterns = [
    path('login/', login, name='login-url'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('valuers/', views.list_valuers, name='valuers'),
    path('valuers/create', views.create_valuer, name='create'),
    path('valuers/<int:pk>', views.update_valuer, name='update'),
    path('valuers/delete/<int:pk>', views.delete_valuer, name='delete'),


]

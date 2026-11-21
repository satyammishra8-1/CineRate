from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),

    #authentication path
    path('register/',views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LoginView.as_view(),name='logout'),

    #reviews path
    path('review/<int:revie_id>/edit',views.edit_review, name='edit_review'),
    path('review/<int:revie_id>/delete',views.edit_review, name='delete_review'),

]


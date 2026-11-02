from django.urls import path

from . import views

urlpatterns= [
    path('', views.event_list_view, name='event_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('event/<int:event_id>/register/', views.register_event_view, name='register_event'),

    path('my_registrations/',views.my_registrations_view,name='my_registrations'),
    path('registration/<int:registration_id>/cancel/',views.cancel_registration_view,name='cancel_registration')

]
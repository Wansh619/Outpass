from django.urls import path
from . import views
urlpatterns=[
    path('home',views.home,name='home'),
    path('',views.intro, name='intro'),
    # path('admin_login',views.admin_login,name='admin_login' ),
    path('Approve',views.Approve,name='Approve')

  

]
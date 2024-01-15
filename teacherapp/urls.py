from django.urls import path
from . import views
urlpatterns=[
   path('',views.home,name='home'),
   path('aboutus',views.aboutus,name='aboutus'),
   path('services',views.services,name='services'),
   path('login',views.login,name='login'),
   path('contactus',views.contactus,name='contactus') 

]
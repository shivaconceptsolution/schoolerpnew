from django.urls import path
from . import views
urlpatterns=[
    path('',views.hello,name='hello'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('stuinfo',views.studentinfo,name='studentinfo'),
    path('stuoutput',views.studentoutput,name='studentoutput'),
    path('addition',views.addition,name='addition'),
    path('additionoutput',views.additionoutput,name='additionoutput'),
    path('swap',views.swap,name='swap'),
    path('swaplogic',views.swaplogic,name='swaplogic'),
    path('marksheet',views.marksheet,name='marksheet'),
    path('radioexample',views.radioexample,name='radioexample'),
    path('checkboxexample',views.checkboxexample,name='checkboxexample'),
    path('dropdownlistexample',views.dropdownlistexample,name='dropdownlistexample'),
    path('listexample',views.listexample,name='listexample')
    
]
from django.urls import path
from . import views
from coursestudent.myviews import Welcome,Fileupload
urlpatterns=[
   # path('',views.index,name='index'),
     path('',Welcome.as_view()),
]
from django.urls import path
from . import views
from coursestudent.myviews import Welcome,Fileupload
from .views import JobCreate,JobList
urlpatterns=[
   # path('',views.index,name='index'),
     path('',Welcome.as_view()),
     path('stuinfo/<int:id>',views.stuinfo,name='stuinfo'),
     path('studetailinfo/<int:id>',views.studetailinfo,name='studetailinfo'),
    # path('fileupload/',views.fileupload,name='fileupload'),
     path('fileupload/',Fileupload.as_view()),
     path('ajaxload',views.ajaxload,name='ajaxload'),
     path('ajaxdata',views.ajaxdata,name='ajaxdata'),
     path('ajaxjquery',views.ajaxjquery,name='ajaxjquery'),
     path('ajaxjquerycode',views.ajaxjquerycode,name='ajaxjquerycode'),
     path('jobcreate',JobCreate.as_view()),
     path('joblist',JobList.as_view())

]
from django.conf.urls import url,include
from users.views import Register,UsersList,UserViewAndEdit
from rest_framework import routers
from django.urls import re_path
from rest_auth.views import PasswordResetConfirmView
from rest_framework_jwt.views import verify_jwt_token

router=routers.DefaultRouter()

urlpatterns=[
    url(r'^signup/$',Register.as_view()),
    url(r'^root/',include('rest_auth.urls')),
    url(r'^list$',UsersList.as_view()),
    url(r'^view&update/$',UserViewAndEdit.as_view()),
    
    # url(r'^', include('django.contrib.auth.urls'))
]
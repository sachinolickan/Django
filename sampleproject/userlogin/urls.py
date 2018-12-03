from django.conf.urls import url
from userlogin.views import RegisterView

urlpatterns=[
    url(r'^REG$',RegisterView.as_view(),name='rg2'),
]
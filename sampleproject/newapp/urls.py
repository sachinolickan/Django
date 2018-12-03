from django.conf.urls import url
from newapp.views import HomeView,LoginView,RegistView,ImageView,DisplayView,DisplayNewView,BootRegisterView,Newloginview
from newapp import views
from userlogin.views import RegisterView
urlpatterns = [
    url(r'^home/',HomeView.as_view(),name='hme'),
    url(r'^Login/',LoginView.as_view(),name='lg'),
    url(r'^Contact/',views.ContactView,name='cn'),
    url(r'^register/',RegistView.as_view(),name='rg'),
    url(r'^upload/',ImageView.as_view(),name='iv'),
    url(r'^display/',DisplayView.as_view(),name='dv'),
    url(r'^New/',DisplayNewView.as_view(),name='new'),
    url(r'^newuser/',BootRegisterView.as_view(),name='newreg'),
    url(r'^signup/',RegisterView.as_view(),name='sign'),
    url(r'^samplelogin/',Newloginview.as_view(),name='smpl')

]
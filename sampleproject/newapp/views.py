from django.shortcuts import render
from django.views.generic import TemplateView,View,CreateView,ListView
from newapp.forms import registForm,imgForm,loginForm
from newapp.models import student,login

# Create your views here.
class HomeView(TemplateView):
    template_name='bt.html'


class BootRegisterView(TemplateView):
    template_name ='registerbootstrap.html'


class LoginView(View):
    template_name='webpage.html'
    def get(self,request):
        return render(request,self.template_name)

def ContactView(request):
    return render(request,'webpage.html')

class RegistView(CreateView):
    template_name ='regist.html'
    form_class = registForm
    success_url = 'success'

class ImageView(CreateView):
    template_name ='img.html'
    form_class=imgForm
    success_url= 'success'

class DisplayView(ListView):
    template_name = 'list.html'
    model = student
    context_object_name = 'lv'


class DisplayNewView(View):
    template_name='listview.html'
    def get(self,request):
        data=student.objects.order_by('-name')
        context= {
            'data':data
        }
        return render(request,self.template_name,context)


class Newloginview(CreateView):
    template_name = 'nw.html'
    form_class = loginForm
    success_url = 'success'

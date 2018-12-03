
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

from django.shortcuts import render,redirect
from django.views.generic import FormView
from django.contrib.auth.models import User
from userlogin.forms import UserForm,EmployeeForm

from userlogin.models import employee

class RegisterView(FormView):
	template_name='userlogin.html'
	form_class = UserForm
	model = User

	def get(self,request,*args, **kwargs):
	    self.object = None
	    form_class = self.get_form_class()
	    user_form = self.get_form(form_class)
	    cust_form = EmployeeForm()
	    return self.render_to_response(self.get_context_data(form1=user_form, form2=cust_form))


	def post(self,request,*args,**kwargs):
	    self.object = None
	    form_class = self.get_form_class()
	    user_form = self.get_form(form_class)
	    cust_form = EmployeeForm(self.request.POST,self.request.FILES)
	    if (user_form.is_valid() and cust_form.is_valid()):
	        return self.form_valid(user_form, cust_form)
	    else:
	        return self.form_invalid(user_form, cust_form)

	def get_success_url(self, **kwargs):
	    return ('success')

	def form_valid(self, user_form, cust_form):
	    self.object = user_form.save()
	    self.object.is_staff=True
	    self.object.save()
	    cust_obj= cust_form.save(commit=False)
	    cust_obj.usr_data = self.object
	    cust_obj.save()
	    return redirect('/login/')

	def form_invalid(self, user_form, cust_form):
	    return self.render_to_response(self.get_context_data(form1=user_form, form2=cust_form))





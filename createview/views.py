from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django import forms


#create your views here

class StudentCreateView(CreateView):
    model= Student
    fields= ['name','email','password']
    success_url= '/thanks/'
    template_name= 'school/sform.html' #This field is optional we just wrote it to tell that we can go by the cusstom template instead of the template given by student_form.html, which is default template
    def get_form(self):#we are overriding this default method
        form= super().get_form()
        form.fields['name'].widget= forms.TextInpt(attrs={
            'class':'myclass' #you can add bootstrap classes through this
        })
        form.fields['password'].widget= forms.TextInpt(attrs={
            'class':'mypass'
        })#this adds the myclass class to the form field with name 'password'
        return form
class ThanksTemplateView(TemplateView):
    template_name='school/thanks.html'    

class StudentDetailView(DetailView):
    model= Student   


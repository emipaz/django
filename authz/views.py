

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.http import urlencode






class OpenView(View) :
    def get(self, request):
        return render(request, 'authz/main.html')

class ApereoView(View) :
    def get(self, request):
        return render(request, 'authz/main.html')

class ManualProtect(View) :
    def get(self, request):
        if not request.user.is_authenticated :
            loginurl = reverse('login')+'?'+urlencode({'next': request.path})
            return redirect(loginurl)
        return render(request, 'authz/main.html')

class ProtectView(LoginRequiredMixin, View) :
    def get(self, request):
        return render(request, 'authz/main.html')

from django.http import HttpResponse

class DumpPython(View) :
    def get(self, req):
        resp = "<pre>\nUser Data in Python:\n\n"
        resp += "Login url: " + reverse('login') + "\n"
        resp += "Logout url: " + reverse('logout') + "\n\n"
        if req.user.is_authenticated:
            resp += "User: " + req.user.username + "\n"
            resp += "Email: " + req.user.email + "\n"
        else:
            resp += "User is not logged in\n"

        resp += "\n"
        resp += "</pre>\n"
        resp += """<a href="/authz">Go back</a>"""
        return HttpResponse(resp)

############ para nuevo usuario
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login, authenticate, logout
#from django.contrib.auth.decorators import login_required
####################

from django.http import HttpResponseRedirect
from django.template import RequestContext

def nuevo_usuario(request):
    if request.method == "POST":
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect("/")
    else:
        formulario = UserCreationForm()
    return render(request,template_name="authz/nuevo_usuario.html",context={"formulario":formulario})



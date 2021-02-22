# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request) :

    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 :
        del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    oldval = request.COOKIES.get('dj4e_cookie', None)
    if oldval !=  'f4adf97f':
        resp.set_cookie('dj4e_cookie', '88ba8576', max_age=1000)
    return resp


# resp.set_cookie('dj4e_cookie', 'f4adf97f', max_age=1000)
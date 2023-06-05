from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from portal.models import UserAccount
from portal.forms import UserAccountForm

import os

def index_page(req):
    if not req.session.has_key('user_id'):
        return redirect('/login/')
    
    flag = os.getenv('FLAG', 'REDACTED')
    if req.session['user_is_admin']:
        return HttpResponse(f'Congratulations: {flag}')
    return HttpResponse('No Flag')

def login_page(req):
    print(req.session.get('user_id'))
    if req.session.has_key('user_id'):
        return redirect('/')

    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        if not username or not password:
            messages.error(req, 'Username/password is empty.')
        try:
            user = UserAccount.objects.get(username=username, password=password)
            req.session['user_id'] = user.pk
            req.session['user_is_admin'] = user.is_admin
            return redirect('/')
        except:
            messages.error(req, 'Username/password is wrong.')

    return render(req, 'login.html')

def logout_page(req):
    req.session.flush()
    return redirect('/login')

def register_page(req):
    if req.session.has_key('user_id'):
        return redirect('/')

    if req.method == 'POST':
        form = UserAccountForm(req.POST)
        if form.is_valid() and form.save():
            messages.success(req, 'User created successfully.')
            return redirect('/login')
        messages.error(req, 'Failed to create new user.')
    return render(req, 'register.html')

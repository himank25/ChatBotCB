#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from dashboard.models import Messages


def index(request):
	context_dict = {}
	context_dict['hi'] = 'hi'
	context_dict['data'] = Messages.objects.all()	

	return render(request, 'dashboard/index.html', context_dict)

def login(request):
	context_dict = {}
	return render(request, 'dashboard/login.html', context_dict)
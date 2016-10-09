#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings


def index(request):
	context_dict = {}
	context_dict['hi'] = 'hi'
	return render(request, 'dashboard/index.html', context_dict)



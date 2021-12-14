from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Rating
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.

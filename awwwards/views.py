from .models import Profile, Post, Rating
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .serializers import ProfileSerializer, UserSerializer, PostSerializer
from django.contrib.auth import login, authenticate
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, PostForm, UpdateUserForm, UpdateUserProfileForm, RatingsForm
import random

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Course


def index(request):
    courses = Course.objects.all()
    return HttpResponse(courses)

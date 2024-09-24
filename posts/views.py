from django.shortcuts import render
from django.http import HttpResponse
import random


def test_view(reequest):
    return HttpResponse(f"Hello World!{random.randint(0,1000)}")


def main_page_view(request):
    return render(request,'base.html')






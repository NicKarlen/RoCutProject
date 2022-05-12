from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.utils import timezone
from .models import Waitlist

def index(request):
  return render(request, 'home/index.html',)

def waiting_list(request):
  return render(request, 'home/waiting_list.html')

def about(request):
  return render(request, 'home/about.html')

def add_waitlist(request):
  try:
    waitlist = Waitlist(join_date=timezone.now(), person_name=request.POST["name"],email=request.POST["email"],confirmation_email_sent=False)
  except:
    # better exception handeling needed!!!!!!.
    return HttpResponseRedirect(reverse('home:about', ))
  else:
    waitlist.save()
    # Always return an HttpResponseRedirect after successfully dealing with POST data.
    # This prevents data from being posted twice if user hits the Back button.
    return HttpResponseRedirect(reverse('home:index', ))
  
  
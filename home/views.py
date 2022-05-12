from django.shortcuts import render

def index(request):
  return render(request, 'home/index.html',)

def waiting_list(request):
  return render(request, 'home/waiting_list.html')

def about(request):
  return render(request, 'home/about.html')

def add_waitlist(request):

  print(request)
  return render(request, '<h1>you have joined the waitlist</h1>')
from django.shortcuts import render

def index(request):
  return render(request, 'home/index.html',)

def waiting_list(request):
  return render(request, 'home/waiting_list.html')

def about(request):
  return render(request, 'home/about.html')

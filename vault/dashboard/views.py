from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def clusters(request):
    return render(request, 'clusters.html')
def jobs(request):
    return render(request, 'jobs.html')
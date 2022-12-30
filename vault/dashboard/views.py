from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def add_cluster(request):
    return render(request, 'add_cluster.html')
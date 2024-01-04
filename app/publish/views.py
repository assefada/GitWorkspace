from django.shortcuts import render

# Create your views here.

def index(request):
    """Render the landing page for the publish app"""
    return render(request, 'publish/index.html')
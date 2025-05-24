from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    return render(request, 'pages/contact.html')

def website_view(request):
    return render(request, 'pages/website.html')

def template_view(request):
    return render(request, 'pages/template.html')
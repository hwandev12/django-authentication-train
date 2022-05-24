from django.shortcuts import render


# create home template
def home(request):
    return render(request, 'pages/home.html')

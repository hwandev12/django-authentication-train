from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView
from .forms import CustomUserModelCreate


# create home template
def home(request):
    return render(request, 'pages/home.html')


# create signup view
class SignUpView(CreateView):
    form_class = CustomUserModelCreate
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse('login')

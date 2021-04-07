from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import auth

# from .forms import SignUpForm
# def index(request):
#     template = loader.get_template('user/dashboard.html')
#     context = {
#         'page_description': 'This is the user dashboard. It will display \
#           user info and diaries written (or it will redirect to the login page).',
#     }
#     return HttpResponse(template.render(context, request))
def login_signup(request):
  context = {
    "page_description" : "This is the first page of a service that allows users to log in or sign up for membership."
  }
  return render(request, 'user/login_signup.html', context)
  
  pass

def login(request):
  if request.method == "POST":
    email = request.POST['email']
    password = request.POST['password']
    username = request.POST['username']
    user = auth.authenticate(email=email, password=password, username=username)
  pass

def logout(request):
  pass

def signup(request):
  if request.mothod=="POST":
    form = SignUpForm(request.POST)
    if form.is_valud():
      form.save()
      email = form.cleaned_data.get('email')
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password')
    user = User.objects.create_user(username=request.POST['email'], password=request.POST['password'])

  pass

def setting(request):
  pass

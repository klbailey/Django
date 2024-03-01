from django.shortcuts import render, redirect
from .forms import MyForm

# Create your views here.
# Index view takes request object as param; receives http request and 'request object has info about 
# request made by user
def index(request):
    # data dictionary is created having key value pairs
    data = {
        # then in html (here is index.html) use {{ variable }} to insert values dynamically
        'first_name': 'Kathy',
        'last_name': 'Bailey Hines',
        'favorite_food': 'Paella',
        'vacation_destination': 'Surfing'
    }
    return render(request, 'main_app/index.html', data)

def form_view(request):
    # If current request method is a post request
    if request.method == 'POST':
        # Create instance of MyForm and populates w/data from post request
        form = MyForm(request.POST)
        # after form created check if form is valid
        if form.is_valid():
            # get cleaned data from form (cleaned/processed by form validation)
            data = form.cleaned_data
            # render template submitted_data.html
            return render(request, 'main_app/submitted_data.html', {'data': data})
    # if request method isn't post like a GET request new instance of form created
    else:
        form = MyForm()
    # view renders template form.html and passes form instance as context
    return render(request, 'main_app/form.html', {'form': form})


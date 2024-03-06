#main_app>views.py
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import UserProfileForm
from .models import UserProfile


# Create your views here.
# Handle form submission, save user data to the database, and display user names on the homepage.
def index(request):
    # if form is submitted
    if request.method == 'POST':
        # creates an instance of the UserProfileForm by passing the form data 
        # (request.POST) to it, necessary for processing the submitted form.
        form = UserProfileForm(request.POST)
        # checks if the submitted form data is valid-meets the defined rules and requirements in the form class.
        if form.is_valid():
            # If the form is valid, save the form data (user info) to the database.
            form.save()
            # After successfully saving form, redirect user back to the homepage (index.html)
            return redirect('home')
        # If request not POST (a GET request), create a new instance of the UserProfileForm to be used
        # for rendering the form in the template.
    else:
        form = UserProfileForm()
    
    # Fetch all existing user profiles from database
    user_profiles = UserProfile.objects.all()

    # Renders index.html template, passing form and user profiles as context variables for use in the template.
    return render(request, 'main_app/index.html', {'form': form, 'user_profiles': user_profiles})

# New view takes request object and user_id param extracted from URL
def user_detail(request, user_id):
    # fetch UserProfile from database; if no user_id found, returns error
    user_profile = get_object_or_404(UserProfile, id=user_id)
    # If user found render user_detail.html passing user_profile as context variable
    return render(request, 'main_app/user_detail.html', {'user_profile': user_profile})
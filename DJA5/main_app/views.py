# main_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
# as using 'DIRS': [os.path.join(BASE_DIR, 'templates')], in settings:
import os

def display_data(request):
    print(request)
    # Check if 'number' is in the session; if not, initialize it to 0
    if 'number' not in request.session:
        request.session['number'] = 0

    # Increment the number based on the URL path
    if request.path == '/addtwo/':
        # Increment by two for '/addtwo' URL
        request.session['number'] += 2
    elif request.path == '/reset/':
        # Reset the number to 0 for '/reset' URL
        request.session['number'] = 0
    else:
        # Increment by one for other URLs
        request.session['number'] += 1

    # Get the current number from the session
    number = request.session['number']

    print(f"Current number: {number}")

    # Pass the number to the template
    context = {'number': number}
    return render(request, 'main_app/data.html', context)

# def set_session(request):
#     # Set a session variable
#     request.session['favorite_color'] = 'blue'
#     return HttpResponse("Favorite color set to blue.")

# def get_session(request):
#     # Get the session variable
#     favorite_color = request.session.get('favorite_color', 'default_color')
#     return HttpResponse(f"Favorite color is {favorite_color}.")


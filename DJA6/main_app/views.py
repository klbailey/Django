#main_app>views.py
from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    #Fetch all posts from database
    posts = Post.objects.all()

    #Pass posts w/form to template
    # 'form': PostForm() create instance of PostForm class in dictionary with key 'form'
    my_dict = {'insert_me': "From views.py!", 'form': PostForm(), 'posts': posts}
    return render(request, 'main_app/index.html', context=my_dict)

# processes form submission, checks validity, saves post to database
def addpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        print("Submitted data:", request.POST)
        if form.is_valid():
            form.save()
            print("Post saved successfully")
            return redirect('index')  # Redirect to the index view after successfully adding a post
        
    posts = Post.objects.all()
    # If the form is not valid or it's a GET request, render the index template with the form
    my_dict = {'insert_me': "From views.py!", 'form': PostForm(), 'posts': posts}
    return render(request, 'main_app/index.html', context=my_dict)


from django.shortcuts import render
from django.http import HttpResponse    #Not being used
import os

# Create your views here.

def index(request):
    context_dictionary = {'insert_here': os.getcwd()} #my webpage i.e. the index.html has a variable insert_here
    #so for its values I pass a dictionary if there are more variables use this same key-value dictionary :D
    path_to_index_html = os.path.join(os.getcwd(),"templates","first_app","index.html" )
    return render(request, path_to_index_html, context = context_dictionary)
    #render returns the WEBPAGE YOU WANT  the default folder was set in settings.py in TEMPLATES
    # return HttpResponse('This was old stuff')

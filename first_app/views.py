from django.shortcuts import render
from django.http import HttpResponse    #Not being used
import os
from .models import Topic, Webpage, AccessRecord


# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by("date")
    context_dictionary = {'acc_rec_list':webpage_list}
    path_to_index_html = os.path.join(os.getcwd(),"templates","first_app","index.html" )
    return render(request, path_to_index_html, context = context_dictionary)
    #render returns the WEBPAGE YOU WANT  the default folder was set in settings.py in TEMPLATES
    # return HttpResponse('This was old stuff')

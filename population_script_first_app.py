#This can be used as a reference to populate the SQL database through django using a python script

#This is necessary stuff just do it
#see the location of this py file very important!!!! it should be JUST inside the root directory! else you modify the
#kingpin.settings accordingly! here kingpin is the main project name
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kingpin.settings')

#setup django
import django
django.setup()


#fake data generator
import random
from faker import Faker
from first_app.models import Topic, Webpage, AccessRecord


fakegen = Faker()
topic_names = ['Search', 'Social', 'Marketplace', 'News', 'Games']  #I took my own topic topic_names

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topic_names))[0]   #[0] bakchodi with tuple-shit
    t.save()
    return t



def populate(N=5):
    #see documentation of faker for more!

    for _ in range(N):
        top = add_topic()  #anyone of the genres in topic_names is given to top randomly
        fake_name = fakegen.company()
        fake_url = fakegen.url()
        fake_date = fakegen.date()  #note this will be of form of DateField (as desired) and NOT Charfield


        #note that topic is Foreign key to Topic Database Blueprint so we gotta pass an object to that class
        webpg = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]  #now a top with a random genre creates  a webpage

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]  #now a given webpg aith a rando top genre gives a access_record


if __name__ == '__main__':
    print("Started Populating the Models")
    populate(20)
    print("Done Populating")

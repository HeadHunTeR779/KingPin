#This can be used as a reference to populate the SQL database through django using a python script

#This is necessary stuff just do it
#see the location of this py file very important!!!!
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
        top = add_topic()
        fake_name = fakegen.company()
        fake_url = fakegen.url()
        fake_date = fakegen.date()  #note this will be of form of DateField (as desired) and NOT Charfield


        #note that topic is Foreign key to Topic Database Blueprint so we gotta pass an object to that class
        webpg = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("Started Populating the Models")
    populate(20)
    print("Done Populating")

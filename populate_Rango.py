import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                       'TWD_project.settings')
import django
django.setup()
from Rango.models import Category, Page
def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    python_pages = [
        {"title": "Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/","views":"8"},
        {"title":"How to Think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/","views":"28"},
        {"title":"Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/","views":"1"} ]

    django_pages = [
         {"title":"Official Django Tutorial",
          "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/","views":"11"},
         {"title":"Django Rocks",
          "url":"http://www.djangorocks.com/","views":"13"},
         {"title":"How to Tango with Django",
          "url":"http://www.tangowithdjango.com/","views":"14"} ]

    other_pages = [
        {"title":"Bottle",
            "url":"http://bottlepy.org/docs/dev/","views":"28"},
         {"title":"Flask",
          "url":"http://flask.pocoo.org","views":"2"} ]

    cats = {"Python": {"pages": python_pages, "likes": 64, "views": 168},
             "Django": {"pages": django_pages, "likes": 32, "views": 64 },
             "Other Frameworks": {"pages": other_pages, "likes": 16, "views": 32} }

     # If you want to add more catergories or pages,
     # add them to the dictionaries above.

     # The code below goes through the cats dictionary, then adds each category,
     # and then adds all the associated pages for that category.
     # if you are using Python 2.x then use cats.iteritems() see
     # http://docs.quantifiedcode.com/python-anti-patterns/readability/
     # for more information about how to iterate over a dictionary properly.

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["likes"], cat_data["views"])
        for p in cat_data["pages"]:
             add_page(c, p["title"], p["url"], p["views"])

     # Print out the categories we have added.
    for c in Category.objects.all():
         for p in Page.objects.filter(category=c):
             print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
     p = Page.objects.get_or_create(category=cat, title=title)[0]
     p.url=url
     p.views=views
     p.save()
     return p

def add_cat(name,likes,views):
     c = Category.objects.get_or_create(name=name)[0]
     c.likes=likes;
     c.views=views;
     c.save()
     return c

 # Start execution here!
if __name__ == '__main__':
     print("Starting Rango population script...")
     populate()
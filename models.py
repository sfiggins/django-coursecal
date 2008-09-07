from django.db import models
from django.contrib.localflavor.us.models import USStateField

class Location(models.Model):
    """ A city or place name. """
    name = models.CharField(max_length=40)
    url = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=40, default="Lawrence")
    state = USStateField(default="KS")
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    directions = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Course(models.Model):
    """ Course title and description.  Will be displayed on own page """
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    lead = models.TextField('short description') 
    description = models.TextField('web page content')
    
    
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/course/detail/%s/" % self.slug
    
class CourseEvent(models.Model):
    """ Courses may be held multiple times over multiple dates.  This is a specific course date and location"""
    course = models.ForeignKey(Course)
    location = models.ForeignKey(Location)
    date = models.DateField('start date')
    start_time=models.TimeField('start time')
    end_time = models.TimeField('end time')
    topic = models.CharField(max_length=100, blank=True, null=True)
    presenter = models.CharField(max_length=100, blank=True, null=True)
    details = models.TextField('Event details', blank=True, null=True)

    def __unicode__(self):
        return "%s - %s" % (self.course, self.date.strftime('%m/%d/%Y'))

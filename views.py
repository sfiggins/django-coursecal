# Create your views here.
from django.template import Template, Context
from django.shortcuts import render_to_response, get_object_or_404
from coursecal.models import Course, CourseEvent
from datetime import date



def upcoming_event_list():
    return CourseEvent.objects.filter(date__gte=date.today())
    
def upcoming_event_list_print(eventlist):
    t = Template("""<ul>
    {% for e in events %}
    <li>{{e.date|date:"m/d"}} - <a href="event.html">{{e.course.title}}</a></li>
    {% endfor %}
</ul>""")
    c = Context({"events": eventlist[:4]})
    t.render(c)

def event_calendar(request):
    event_list = upcoming_event_list().order_by('date', 'start_time')

    return render_to_response('courses/calendar.html', 
        {'courseevents': event_list})

def course_by_slug(request, slug_id):
    c = get_object_or_404(Course, slug=slug_id)
    c_event_list = CourseEvent.objects.filter(course__exact=c).filter(date__gte=date.today()).order_by('date')
    return render_to_response('courses/detail.html', {'course': c, 'events': c_event_list})

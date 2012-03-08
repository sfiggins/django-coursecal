from django.contrib import admin
from coursecal.models import Location, Course, CourseEvent


class LocationAdmin(admin.ModelAdmin):
    pass

class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class CourseEventAdmin(admin.ModelAdmin):
    ordering = ['-date']
    date_hierarchy = 'date'
    list_display = ('course', 'date', 'topic', 'location')

admin.site.register(Location, LocationAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseEvent, CourseEventAdmin)

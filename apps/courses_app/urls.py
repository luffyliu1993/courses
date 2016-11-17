from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^get_info$',views.get_info),
    url(r'^delete/(?P<id>[0-9]+?)$',views.delete),
    url(r'^delete_course/(?P<id>[0-9]+?)$',views.delete_course),
    url(r'^comment/(?P<id>[0-9]+?)$',views.render_comment),
    url(r'^add_comment/(?P<course_id>[0-9]+?)$',views.add_comment)
]

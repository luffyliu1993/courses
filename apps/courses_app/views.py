from django.shortcuts import render,redirect
from .models import Course,Comment
from django.contrib import messages

# Create your views here.
def index(request):
    data = {
        'courses':Course.objects.all()
    }
    return render(request,'courses_app/index.html',data)

def get_info(request):
    if len(request.POST['name']) > 0:
        course_name = request.POST['name']
        desc = request.POST['desc']
        course = Course.objects.create(course_name=course_name,description=desc)
    else:
        messages.add_message(request,messages.ERROR, 'Course Name Cannot Be Empty')
    return redirect('/')

def delete(request,id):
    data = {
        'course':Course.objects.get(id=id)
    }
    return render(request,'courses_app/delete.html',data)

def delete_course(request,id):
    if request.GET['action'] != 'No':
        Course.objects.filter(id=id).delete()
    return redirect('/')

def render_comment(request,id):
    data = {
        'course_id':id,
        'course_name': Course.objects.get(id=id).course_name,
        'comments': Comment.objects.filter(course__id = id)
    }
    return render(request,'courses_app/comment.html',data)

def add_comment(request,course_id):
    if len(request.POST['comment']) > 0:
        Comment.objects.create(comment=request.POST['comment'],course=Course.objects.get(id=course_id))
    return redirect('/comment/'+course_id)

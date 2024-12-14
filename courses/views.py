from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Course, Student
from .forms import StudentRegistrationForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_register(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if course.current_enrolled >= course.maximum_capacity:
        return HttpResponse("<h1>This course is full!</h1><a href='/'>Back to Course List</a>")

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, available_courses=Course.objects.filter(id=course_id))
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            student, created = Student.objects.get_or_create(name=name, email=email)
            if course in student.enrolled_courses.all():
                return HttpResponse(
                    "<h1>You are already enrolled in this course!</h1><a href='/'>Back to Course List</a>")
            else:
                student.enrolled_courses.add(course)
                course.current_enrolled += 1
                course.save()
                return HttpResponse("<h1>Successfully enrolled in the course!</h1><a href='/'>Back to Course List</a>")
                print(course)
            return redirect('course_list')

    else:
        form = StudentRegistrationForm(available_courses=Course.objects.filter(id=course_id))
    return render(request, 'courses/course_register.html', {'form': form, 'course': course})

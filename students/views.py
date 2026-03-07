

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

def home(request):
    students = Student.objects.all()
    return render(request, 'students/home.html', {'students': students})
def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'students/add.html', {'form': form})

def update_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'students/update.html', {'form': form})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('home')
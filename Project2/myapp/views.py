from django.shortcuts import render,redirect

# Create your views here.
from .models import Student

def home(request):
    return render(request,'create.html')

def create(request):
    st=Student()
    name=request.GET.get('name')
    roll=request.GET.get('roll')
    city=request.GET.get('city')
    marks=request.GET.get('marks')
    st.name=name
    st.roll=roll
    st.city=city
    st.marks=marks
    st.save()
    return render(request,'create.html')

def read(request):
    students=Student.objects.all()
    return render(request,'read.html',{'students':students})

# views read specific student
def read_student(request):
    roll = request.GET.get('roll')
    try:
        student = Student.objects.get(roll=roll)
        return render(request, 'read_students.html', {'student': student})
    except Student.DoesNotExist:
        return render(request, 'read_students.html', {'error': 'Student not found'})
    
#update student

def update(request):
    roll = request.GET.get('roll')
    if roll:
        try:
            student = Student.objects.get(roll=roll)
            if 'name' in request.GET and 'city' in request.GET and 'marks' in request.GET:
                # Update student details
                student.name = request.GET.get('name')
                student.city = request.GET.get('city')
                student.marks = request.GET.get('marks')
                student.save()
                # return redirect('readstudent')  # Redirect after successful update
            return render(request, 'update_student.html', {'student': student})
        except Student.DoesNotExist:
            return render(request, 'update_student.html', {'error': 'Student not found'})
    return redirect('read_student')  # Redirect if not a GET reques

# delete 
def delete(request):
    roll = request.GET.get('roll')
    if roll:
        try:
            student = Student.objects.get(roll=roll)
            student.delete()
            return redirect('read_student')
        except Student.DoesNotExist:
            return render(request, 'delete_student.html', {'error': 'Student not found'})
    return redirect('read_student')  # Redirect if not a GET request




from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Course
student = Student()

def index(request):
    return render(request, 'login/login.html')

# Create your views here.
def test(request):
    return HttpResponse("Hello, test")

def select(request):

    course = Course.objects.all()
    context = {'course': course}

    if request.method == 'POST':
        user = request.POST.get('username')
        pw = request.POST.get('password')

    student = Student.objects.get(stuName=user)
    context['student']=student

    if student.stuPasswd==pw:
        return render(request, 'login/select.html', context)
    else:
        return render(request, 'login/wrong.html',{'wrong':'your password is wrong'})

def result(request):
    if request.method == "POST":

        wrongtext ={"wrong":''}
        stu = request.POST.get('stu')
        student=Student.objects.get(stuName=stu)
        print(student)
        couSel_list = request.POST.getlist('couSel')
        for i in couSel_list:
            course = Course.objects.get(couName=i)
            if course.couLeftNum==0:
                wrongtext["wrong"]+=course.couName+"已满"
            if course.couName in student.stuCou:
                wrongtext["wrong"] += course.couName + "已选"
            else:
                course.couAllNum+=1
                course.couLeftNum-=1
                if course.couPer:
                    course.couPer +=student.stuName
                else:
                    course.couPer+=','+student.stuName
                if student.stuCou:
                    student.stuCou += ',' + course.couName
                else:
                    student.stuCou+=course.couName
        print(wrongtext)
        if wrongtext["wrong"]:
            return render(request,'login/wrong.html',wrongtext)
        print (student.stuCou)
        stuCou_list = student.stuCou.split(',')
        student.save()
        course.save()
        return render(request, 'login/result.html',{'stuCou_list':stuCou_list,'student':student})
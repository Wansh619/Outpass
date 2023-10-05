from django.shortcuts import render 
from django.shortcuts import redirect
from .models import Students
from django.contrib import messages
import smtplib as sm


# PASSWORD='cmextopvyhmqmmlp'
# EMAIL='unitycreator619@gmail.com'
# SERVER= sm.SMTP('smtp.gmail.com',587)
# SERVER.starttls()


# def sendmsg(email):
#     SERVER.login(EMAIL,PASSWORD)
#     SERVER.quit()
#     return SERVER.sendmail(EMAIL,email,MSG)



# def passwordchecker(password):
#     if password.len()>8:







def intro(request):
    return render(request,'intro.html')



def home(request):
    if request.method=='POST':
        name=request.POST['name']
        roll_no= request.POST['roll_no']
        reasons=request.POST['reasons']
        email=roll_no + "@lnmiit.ac.in"


        if Students.objects.filter(name=name ,reasons=reasons ).exists():
             messages.info(request,"YOUR SAME REQUEST IS ALREADY THERE")
             return redirect("home")
        elif 
        else:
            student=Students(name=name,roll_no=roll_no,reasons=reasons,email=email)
            student.save()
            messages.info(request,"YOUR REQUEST HAS GOT REGISTERED")
            return redirect('home')
    else:
        return render(request,'index.html')
    


def Approve(request):
    if request.method=='POST':
        Approve_students=request.POST.get('Approved_students')
        if Approve_students=='Reject':
            Students.objects.all().delete()
            return redirect('Approve')

        
        Students.objects.filter(email=Approve_students).delete()
        messages.info(request,"APPROVED")
        return redirect('Approve')
    else:
         students =Students.objects.all()
         return render(request,'Approve.html',{'students':students})
    
 
   




# Create your views here.

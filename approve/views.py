from django.shortcuts import render
from form.models import Students
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

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
    
 
   
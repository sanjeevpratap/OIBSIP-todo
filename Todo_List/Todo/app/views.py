from django.shortcuts import render
from .models import Task
def main(request):
    success=False
    name='Sanjeev'
    if request.method== "POST":
        title=request.POST['title']
        desc=request.POST['desc']
        dead=request.POST['dead']
        pro=Task.objects.create(Title=title,Desc=desc,dead=dead)
        success=True
    d={'success':success,'name':name}

    return render(request,'main.html',d)

def tasks(request):
    allTasks=Task.objects.all()
    #print(allTasks)
    d={'tasks':allTasks}
    return render(request,'tasks.html',d)

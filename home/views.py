from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect , HttpResponse
from django.utils import timezone
from home.models import Todo
# Create your views here.   

def home(request):
    todo_item = Todo.objects.all().order_by("-added_date")
    
    return render(request,'index.html', {
        'todo_items': todo_item
    })

def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']
    created_obj = Todo.objects.create(added_date = current_date , text = content )
    len_of_todos = Todo.objects.all().count()
    return HttpResponseRedirect('/')

def delete_todo(request,todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
    
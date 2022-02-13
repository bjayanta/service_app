from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import TodoForm
from .models import Todo
from django.contrib import messages

# Create your views here.
def index(request):
    records = Todo.objects.all()
    return render(request, 'todo/index.html', {'records': records})

def create(request):
    todoForm = TodoForm()
    return render(request, 'todo/create.html', {'todoForm': todoForm})

def store(request):
    if request.method == 'POST':
        todoForm = TodoForm(request.POST)

        # check validation
        if todoForm.is_valid():
            # collect all input
            label = todoForm.cleaned_data['label']
            status = todoForm.cleaned_data['status']
            reminder = todoForm.cleaned_data['reminder']

            # save 
            todo = Todo(label=label, status=status, reminder=reminder)
            todo.save()

            # message
            messages.add_message(request, messages.SUCCESS, 'Todo has been saved successfully.')

    # redirect
    return redirect('todo.create')

def edit(request, id):
    data = Todo.objects.get(pk=id)
    todoForm = TodoForm(instance=data)
    
    return render(request, 'todo/edit.html', {'todoForm': todoForm, 'id': id})

def update(request, id):
    return HttpResponse(f'Todo ID is {id}')
    
def show(request):
    pass

def delete(request):
    pass

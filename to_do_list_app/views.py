
from django.shortcuts import render, redirect, get_object_or_404
from .models import To_Do_List


# Display all tasks
def home(request):
    data = To_Do_List.objects.all().order_by('-created')
    return render(request, 'home.html', {'data': data})


# Add a new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            To_Do_List.objects.create(
                title=title,
                description=description
            )
            return redirect('home')

    return render(request, 'add_task.html')


# Edit an existing task
def edit_task(request, id):
    task = get_object_or_404(To_Do_List, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            task.title = title
            task.description = description
            task.save()
            return redirect('home')

    return render(request, 'edit_task.html', {'task': task})


# Mark task as completed or pending
def toggle_task(request, id):
    if request.method == 'POST':
        task = get_object_or_404(To_Do_List, id=id)
        task.done = not task.done
        task.save()

    return redirect('home')


# Delete a task
def delete_task(request, id):
    if request.method == 'POST':
        task = get_object_or_404(To_Do_List, id=id)
        task.delete()

    return redirect('home')

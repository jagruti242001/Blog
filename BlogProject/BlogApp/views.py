from django.shortcuts import render , redirect

from . models import BlogModel

# Create your views here.

def home_view(request):
    blogs = BlogModel.objects.all()

    context = {'blogs':blogs}
    return render(request , 'BlogApp/home.html' , context)


def addblog_view(request):
    if request.method =='POST':
        new_title = request.POST['title']
        new_desc = request.POST['desc']
        blog = BlogModel(title = new_title  , desc = new_desc)
        blog.save()

        return redirect('home')
    return render(request , 'BlogApp/addblog.html')


def deleteblog_view(request , id):
    blog = BlogModel.objects.get(id = id)
    blog.delete()

    return redirect('home')


def updateblog_view(request , id):
    blog = BlogModel.objects.get(id = id)
    context = {'blog':blog}

    if request.method == 'POST':
        updated_title = request.POST['title']
        updated_desc = request.POST['desc']
        
        blog.title = updated_title
        blog.desc = updated_desc
        blog.save()

        return redirect('home')

    return render(request , 'BlogApp/updateblog.html' , context)

    
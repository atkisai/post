import this

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils import timezone
from app.forms import PostForm
from app.models import Post
from django.shortcuts import redirect

def index(request):
    posts = Post.objects.filter()
    return render(request, 'index.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def delete(request, id):
    instance = Post.objects.get(id=id)
    instance.delete()
    return redirect('index')

# def delete(request, pk):
#     def delete_product(request, pk):
#         if request.method == "POST":
#               if form.is_valid(): product = form.delete(commit=False)
#                  product.delete()
#               return redirect('index', pk=product.pk)
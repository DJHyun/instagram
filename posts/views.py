from django.shortcuts import render,redirect
from .forms import PostModelForm
from .models import Post


# Create your views here.
def create(request):
    # 만약, POST 요청이 오면
    if request.method == 'POST':
        # 글을 작성하기.
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('posts:list')
            
    # 아니면 (GET 요청이 오면)
    else:
        # post를 작성하는 폼을 가져와 template에서 보여줌.
        form = PostModelForm()
        context = {
            'form': form
        }
        
        return render(request, 'posts/create.html',context)
        
def list(request):
    # 모든 Post를 보여줌
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/list.html', context)
    
def delete(request, post_id):
    Post.objects.get(pk=post_id).delete()
    return redirect('posts:list')


def update(request, post_id):
    po = Post.objects.get(pk=post_id)
    if request.method == "POST":
        # 수정 내용 DB에 반영
        form = PostModelForm(request.POST,request.FILES,instance=po)
        if form.is_valid:
            po = form.save()
            return redirect('posts:list')
        pass
    else:
        # edit 수정 내용 편집
        form = PostModelForm(instance=po)
        context = {
            'form': form
        }
        return render(request, 'posts/update.html',context)
    
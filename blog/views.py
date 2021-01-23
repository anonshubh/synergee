from django.shortcuts import render
from django.views.generic import View

from .models import Post,Member


class ListPost(View):
    """
    On GET: Lists the Post of Author (Interest Wise)
    """
    def get(self,request,author_id,category_id):
        posts = Post.objects.filter(author_id=author_id,category_id=category_id)
        members = Member.objects.all()
        context = {
            'posts':posts,
            'members':members
        }
        return render(request,'blog/list-posts.html',context)


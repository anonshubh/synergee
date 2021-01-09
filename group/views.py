from django.shortcuts import render
from django.views.generic import View

from .models import Member,Interest


class ListProfile(View):
    """
    On GET: Returns the List of Profiles from Database
    """

    def get(self,request):
        members = Member.objects.all()
        context = {
            'members':members
        }
        return render(request,'group/index.html',context)


class DetailProfile(View):
    """
    On GET: Returns the Details on Specific Profile
    """

    def get(self,request,id):
        pass

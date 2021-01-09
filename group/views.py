from django.shortcuts import render
from django.views.generic import View

from .models import Member,Interest


class ListProfile(View):
    """
    On GET: Returns the List of Profiles from Database
    """

    def get(self,request,format=None):
        pass


class DetailProfile(View):
    """
    On GET: Returns the Details on Specific Profile
    """

    def get(self,request,format=None):
        pass

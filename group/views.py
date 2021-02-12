from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import View
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .models import Member,Interest,Contact
from .forms import ContactForm


class ListProfile(View):
    """
    On GET: Returns the List of Profiles from Database
    """

    def get(self,request):
        members = Member.objects.all()
        form = ContactForm()
        context = {
            'members':members,
            'form':form
        }
        return render(request,'group/index.html',context)
    

    def post(self,request):
        form = ContactForm(request.POST)
        if(form.is_valid()):
            cleaned_data = form.cleaned_data
            form.save()

            email = cleaned_data.get('email',None)
            name = cleaned_data.get('name',None)
            your_message = cleaned_data.get('your_message',None)
            receiver = cleaned_data.get('receiver',None)
            entire_team = cleaned_data.get('entire_team',None)

            receivers_email_list = []

            if entire_team:
                members = Member.objects.all()
                for i in members:
                    receivers_email_list.append(i.email)
            elif not entire_team and receiver:
                receivers_email_list.append(receiver.email)
            
            else:
                raise ValidationError

            send_mail(
                'Contact Mail',
                f'From: {name}\nMessage: {your_message}',
                settings.DEFAULT_FROM_EMAIL,
                receivers_email_list,
                fail_silently=False,
            )
            messages.info(request, 'Your Message has been Sent!')
            return redirect('thank-you')

        raise ValidationError


class DetailProfile(View):
    """
    On GET: Returns the Details on Specific Profile
    """

    def get(self,request,id):
        members = Member.objects.all()
        member = get_object_or_404(Member,pk=id)
        context = {
            'member':member,
            'members':members
        }
        return render(request,'group/profile.html',context)

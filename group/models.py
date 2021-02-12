from django.db import models


class Interest(models.Model):
    """
    Category of One's Interest
    """
    type = models.CharField(max_length=100)
    definition = models.CharField(max_length=150,null=True) 
    familiarity = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.type
    

class Member(models.Model):
    """
    Information/Data of Group Member
    """
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    image = models.URLField()
    email = models.EmailField(max_length=56)
    interests = models.ManyToManyField(Interest)
    github_url = models.URLField(blank=True,null=True)
    linkedin_url = models.URLField(blank=True,null=True)
    instagram_url = models.URLField(blank=True,null=True)
    resume_url = models.URLField(blank=True,null=True)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return str(self.first_name)



class Contact(models.Model):
    """
    Information/Data of Sender
    """
    email = models.EmailField(max_length=56)
    name = models.CharField(max_length=56)
    your_message = models.TextField()
    receiver = models.ForeignKey(Member,on_delete=models.CASCADE,null=True,blank=True)
    entire_team = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return f"From:{self.email}"



from django.db import models


class Interest(models.Models):
    """
    Category of One's Interest
    """
    type = models.CharField(max_length=100)
    familiarity = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.type
    

class Member(models.Model):
    """
    Information/Data of Group Member
    """
    name = models.CharField(max_length=56)
    image = models.URLField()
    email = models.EmailField(max_length=56)
    interests = models.ManyToManyField(Interest)
    github_url = models.URLField(blank=True,null=True)
    linkedin_url = models.URLField(blank=True,null=True)

    def __str__(self):
        return str(self.email)

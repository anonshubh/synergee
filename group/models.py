from django.db import models


class Interest(models.Model):
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
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    image = models.URLField()
    email = models.EmailField(max_length=56)
    interests = models.ManyToManyField(Interest)
    github_url = models.URLField(blank=True,null=True)
    linkedin_url = models.URLField(blank=True,null=True)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return str(self.email)

from django.db import models

from group.models import Member,Interest

class Post(models.Model):
    """
    Attributes of Post Relational Model
    """
    author = models.ForeignKey(Member,on_delete=models.CASCADE)
    category = models.ForeignKey(Interest,on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"Posted By {self.author.first_name}"


    


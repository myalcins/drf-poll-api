from django.db import models
from django.utils import timezone
from django.conf import settings


class Question(models.Model):
    # fields
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    question_text = models.CharField(max_length=240)
    description = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images/poll/questions/', null=True,
                              default=None, blank=True)
    task = models.BooleanField(default=False)
    # is_published = models.BooleanField(editable=False, default=False)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)

    # relations
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str: 
        return self.title


class Choice(models.Model):
    # fields
    id = models.AutoField(primary_key=True)
    choice_text = models.CharField(max_length=120)
    voted = models.IntegerField(default=0, editable=False)

    # relations
    question = models.ForeignKey(
        Question, related_name='choices', on_delete=models.CASCADE)

    class Meta:
        ordering=['pk']

        
class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chosen = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-created']

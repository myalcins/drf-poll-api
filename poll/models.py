from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Question(models.Model):
    # fields
    title = models.CharField(max_length=45)
    question_text = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/poll/questions/', null=True,
                              default=None, blank=True)
    task = models.BooleanField(default=False)
    created_at = models.DateTimeField(editable=False)
    slug = models.SlugField(unique=True, editable=False)

    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def get_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        uniq = slug
        num = 1

        while Question.objects.filter(slug=uniq).exists():
            uniq = '{}-{}'.format(slug, num)
            num += 1

        return uniq

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.slug = self.get_slug()
        return super(Question, self).save(*args, **kwargs)

    def __str__(self) -> str: return self.title


class Choice(models.Model):
    # fields
    choice_text = models.CharField(max_length=200)
    voted = models.IntegerField(default=0, editable=False)
    # relations

    question = models.ForeignKey(
        Question, related_name='choices', on_delete=models.CASCADE)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, editable=False)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        ordering = ['-created']

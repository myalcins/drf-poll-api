from django.contrib import admin
from .models import Choice, Question, Vote

admin.site.register(Question)
admin.site.register(Vote)
admin.site.register(Choice)

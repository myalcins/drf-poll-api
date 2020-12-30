from django import dispatch
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Vote
from django.db import transaction


@transaction.atomic
@receiver(pre_save, sender=Vote, dispatch_uid="unq_identifier")
def del_voted_choice(sender, instance, **kwargs):

    if kwargs['update_fields'] is not None:
        instance = Vote.objects.select_related('chosen').get(pk=instance.pk)
        instance.chosen.voted -= 1
        return instance.chosen.save()


@transaction.atomic
@receiver(post_save, sender=Vote, dispatch_uid="unique_identifier")
def set_choice_vote(sender, instance, created, **kwargs):
    if created:
        instance = Vote.objects.select_related('chosen').get(pk=instance.pk)
        instance.chosen.voted += 1
        return instance.chosen.save()

    if 'chosen' in kwargs['update_fields']:
        instance = Vote.objects.select_related(
            'chosen').get(pk=instance.pk)
        instance.chosen.voted += 1
        return instance.chosen.save()

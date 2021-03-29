from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver, Signal
from .models import Vote
from django.db import transaction


@receiver(pre_delete, sender=Vote, dispatch_uid="unq_id")
def del_voted_choice(sender, instance, **kwargs):
    instance.chosen.voted -= 1
    instance.chosen.save()

@receiver(post_save, sender=Vote, dispatch_uid="unique_")
def vote_choice(sender, instance, created, update_fields, **kwargs):
    if created:
        instance.chosen.voted += 1
        return instance.chosen.save()
    if 'chosen' in update_fields:
        instance.chosen.voted += 1
        instance.chosen.save()

# To decrease old choice's voted count
vote_update = Signal()

@receiver(vote_update, sender=Vote, dispatch_uid="unique_identifier")
def decrease_old_choice_voted(sender, instance, **kwargs):
    instance.chosen.voted -= 1
    return instance.chosen.save()
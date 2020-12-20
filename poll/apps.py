from django.apps import AppConfig


class PollConfig(AppConfig):
    name = 'poll'

    def ready(self) -> None:
        from poll.signals import set_choice_vote, del_voted_choice
        from django.db.models.signals import post_save, pre_save
        from poll.models import Vote

        post_save.connect(set_choice_vote, Vote,
                          dispatch_uid="unique_identifier")
        pre_save.connect(del_voted_choice, Vote,
                         dispatch_uid="unq_identifier")

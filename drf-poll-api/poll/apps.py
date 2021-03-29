from django.apps import AppConfig


class PollConfig(AppConfig):
    name = 'poll'

    def ready(self) -> None:
        import poll.signals
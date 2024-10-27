from django.apps import AppConfig
from django.core.signals import request_finished
from signals import likes_enabled_test, can_vote_test, object_liked

class MyAppConfig(AppConfig):
    def ready(self): 
        request_finished.connect(likes_enabled_test)
        request_finished.connect(can_vote_test)
        request_finished.connect(object_liked)
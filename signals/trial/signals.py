from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading
from .models import Data


import time

# @receiver(post_save, sender=User)
# def signal_handle(sender, instance, created, **kwargs):
#     print(f"Signal handler thread: {threading.current_thread().name}")
#     print("Process starts")
#     time.sleep(5)
#     print("Process ends")

@receiver(post_save, sender = User)
def create(sender, instance, created, **kwargs):
    if created:
        print("Signal: Creating Profile")
        Data.objects.create(user = instance, background = "This is it")
        


from django.db import models
from django.utils import timezone
import datetime


# class waitlist
class Waitlist(models.Model):
  join_date = models.DateTimeField("date join")
  person_name = models.CharField(max_length=80)
  email = models.EmailField("email")
  confirmation_email_sent = models.BooleanField(default=0)

  def __str__(self):
    return self.person_name

  def joined_recently(self):
    return self.join_date >= timezone.now() - datetime.timedelta(days=2)
    
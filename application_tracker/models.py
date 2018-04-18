
from django.contrib.auth.models import User
from django.db import models


class ApplicationStateModel(models.Model):
    """
    Attempting to model the application process
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    application_form_completed = models.BooleanField(default=False)
    dbs_received = models.BooleanField(default=False)
    training1 = models.BooleanField(default=False)
    training2 = models.BooleanField(default=False)

class ApplicationForm(models.Model):
    """
    Modelling the application form
    """
    name = models.CharField(max_length=200)
    applicationState = models.ForeignKey(ApplicationStateModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Reference(models.Model):
    """
    Modelling a reference form
    """
    referee = models.CharField(max_length=200)
    application = models.ForeignKey(ApplicationStateModel, on_delete=models.CASCADE, related_name='related_name')
    received = models.BooleanField(default=False)

    def __str__(self):
        return "Reference for {} from {}".format(
            self.application.name,
            self.referee
        )


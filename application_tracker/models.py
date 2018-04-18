
from django.db import models


class ApplicationStateModel(models.Model):
    """
    Attempting to model the application process
    """

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
    application = models.ForeignKey(ApplicationForm, on_delete=models.CASCADE)

    def __str__(self):
        return "Reference for {} from {}".format(
            self.application.name,
            self.referee
        )


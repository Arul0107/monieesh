from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Session(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    word_accuracy = models.FloatField()
    char_accuracy = models.FloatField()

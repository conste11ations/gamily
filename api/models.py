from django.db import models

# Create your models here.

class Account(models.Model):
    email = models.EmailField(max_length=254)

class Profile(models.Model):
    name = models.CharField(max_length=50)
    level = models.PositiveSmallIntegerField(default=0)
    net_worth = models.IntegerField(default=0)
    stress_level = models.PositiveSmallIntegerField(default=0)
    experience = models.PositiveSmallIntegerField(default=0)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)

class Question(models.Model):
    question = models.CharField(max_length=500)

class Answer(models.Model):
    answer = models.CharField(max_length=500)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    impact = models.JSONField()

class Scenario(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.ForeignKey(Answer, on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
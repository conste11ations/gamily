from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Account(models.Model):
    email = models.EmailField(max_length=254)

class Profile(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(default=0)
    education = models.CharField(max_length=50)
    stress_level = models.PositiveSmallIntegerField(default=0)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    credit_score = models.PositiveSmallIntegerField(default=0)
    net_worth = models.IntegerField(default=0)
    assets_mv = models.IntegerField(default=0)
    liabilities_mv = models.IntegerField(default=0)
    insurance = ArrayField(models.CharField(max_length=10, blank=True)) 
    income =  ArrayField(
        ArrayField(models.IntegerField(), size=2))
    expenses = ArrayField(
        ArrayField(models.IntegerField(), size=2))

class Question(models.Model):
    question = models.CharField(max_length=500)
    category = models.CharField(max_length=100)

class Answer(models.Model):
    answer = models.CharField(max_length=500)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    impact = models.JSONField()
    description = models.CharField(max_length=500, blank=True)

class Scenario(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.ForeignKey(Answer, on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
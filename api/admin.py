from django.contrib import admin
from .models import Account, Profile, Question, Answer, Scenario
# Register your models here.

admin.site.register(Account)
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Scenario)
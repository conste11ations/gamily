from .models import Account, Profile, Question, Answer, Scenario
from rest_framework import serializers


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ['url', 'email']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['url', 'name', 'age', 'stress_level', 'account_id', 'credit_score', 'net_worth', 'assets_mv', 'liabilities_mv', 'insurance', 'income', 'expenses']

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['url', 'question', 'category']

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ['url', 'answer', 'question_id', 'impact', 'description']

class ScenarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scenario
        fields = ['url', 'question_id', 'response', 'profile_id']
        
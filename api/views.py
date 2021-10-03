from django.http import HttpResponse
from .models import Account, Profile, Question, Answer, Scenario
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AccountSerializer, ProfileSerializer, QuestionSerializer, AnswerSerializer, ScenarioSerializer

def index(request):
    return HttpResponse("Index of Gamily API")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all().order_by('id')
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('id')
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Answer.objects.all().order_by('id')
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]

class ScenarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Scenario.objects.all().order_by('id')
    serializer_class = ScenarioSerializer
    permission_classes = [permissions.IsAuthenticated]
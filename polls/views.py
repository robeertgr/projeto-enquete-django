from django.shortcuts import render
from django.http import HttpResponse, response
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return HttpResponse("Olá, este é o meu primeiro site")

def detail(request, question_id):
    return HttpResponse('Esta é a pergunta nº %s' % question_id)  # ou usar {} .format(%question_id)

def results(request, question_id):
    response = ('Estes são os resultados da pergunta nº %s' % question_id)

def vote(request, question_id):
    return HttpResponse('Você está votando na pergunta nº %s' % question_id)
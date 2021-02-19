from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Question , Choice

from django.template import loader

from django.shortcuts import render

def index(request):
    ################ primrera vista version con Httresponse #################
    # return HttpResponse("Hello, world. You're at the polls index.")

    #consulta a la base de datos
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # output = ', '.join([q.question_text for q in latest_question_list])
        # concatena los resultados de la consulta en un  string
    # return HttpResponse(output) esta linea era la segunda version donde enviaba el output

    contexto  = {'latest_question_list': latest_question_list,} # creamos un diccionario
    # ############# Version utilizando loader ###############################
    # template = loader.get_template('polls/index.html')                    #
    # return HttpResponse(template.render(contexto, request))               #
    #########################################################################

    ##### Version utilizando el metodo render del modulo django.shortcuts #####
    return render(request, 'polls/index.html', contexto)


from django.http import Http404


def detail(request, question_id):
    # primera version sin exepciones
    # return HttpResponse("You're looking at question %s." % question_id)

    #### manera tradicional de generar un Http404
    #try:
    #    question = Question.objects.get(pk = question_id) #llama al primary key
    #except Question.DoesNotExist:
    #    raise Http404("No Existe la pregunta")

    ##### atajo ṕara generar el error Http404
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


"""
from django.shortcuts import get_object_or_404, render
# Create your views here.

from .models import Question , Choice

primera vistas del proyecto



def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

cambio a vistas mas complejas

from django.template import loader

from django.http import Http404

from django.shortcuts import get_object_or_404, render

def index(request):
    ################ primrera vista version con Httresponse #################
    # return HttpResponse("Hello, world. You're at the polls index.")

    #consulta a la base de datos
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    # output = ', '.join([q.question_text for q in latest_question_list])
        # concatena los  de la consulta en un  string
    # return HttpResponresultadosse(output) esta linea era la segunda version donde enviaba el output

    contexto  = {'latest_question_list': latest_question_list,} # creamos un diccionario
    # ############# Version utilizando loader ###############################
    # template = loader.get_template('polls/index.html')                    #
    # return HttpResponse(template.render(contexto, request))               #
    #########################################################################

    ##### Version utilizando el metodo render del modulo django.shortcuts #####
    return render(request, 'polls/index.html', contexto)

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

from django.http import HttpResponse , HttpResponseRedirect

from django.urls import reverse

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Vuelva a mostrar el formulario de votación de preguntas.
        return render(request, 'polls/detail.html',
                               {'question'      : question,
                                'error_message' : "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Siempre devuelva un HttpResponseRedirect después de negociar con éxito
        # con datos POST. Esto evita que los datos se publiquen dos veces si un
        # el usuario presiona el botón Atrás.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

"""
################# Modo Vistas Genéricas ####################

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Devolver las últimas cinco preguntas publicadas."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Vuelva a mostrar el formulario de votación de preguntas.
        return render(request, 'polls/detail.html',
                               {'question'      : question,
                                'error_message' : "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Siempre devuelva un HttpResponseRedirect después de negociar con éxito
        # con datos POST. Esto evita que los datos se publiquen dos veces si un
        # el usuario presiona el botón Atrás.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def owner(request):
        return HttpResponse("Hello, world. 88ba8576 is the polls owner.")

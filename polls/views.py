from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    #1. simplest view:
    # return HttpResponse("Hello, world. You're at the polls index.")

    #2. view that uses imput from your model, but still using HttpRequest for output,
    # with the web page's design being hard-coded into the view function  (not good!)
    """
    latest_questions = Question.objects.order_by('-pub_date')[:3]
    string = ('; ').join([q.question_text for q in latest_questions])
    return HttpResponse("The latest questions are: %s" %string)
    """
    #3. view that uses a template, with the loader() function and .render() method. 

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
 
    # view that makes use of a template and the render() shortcut
"""
    latest_question_list = Question.objects.order_by('-pub_date')
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})
"""
    

def detail(request, question_id):
    #q = Question.object.get(id=question_id)
    #question = get_object_or_404(Question, id = question_id)
    return HttpResponse("This is the page for question: %s" % question_id)


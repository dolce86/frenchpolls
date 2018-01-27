from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from .models import Question,Reponse

# Create your views here.
def post_list(request):
	posts = Question.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'frenchpolls/post_list.html', {'posts': posts})

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try :
		q=str(question.id + int(request.POST['page']))
		question = get_object_or_404(Question, pk=q)
		return render(request, 'frenchpolls/detail.html', {'question': question})

	except KeyError :
		return render(request, 'frenchpolls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'frenchpolls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.reponse_set.get(pk=request.POST['choice'])

    except (KeyError, Reponse.DoesNotExist):
        return render(request, 'frenchpolls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))
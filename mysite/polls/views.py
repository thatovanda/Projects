from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question
from .models import Company
from .forms import *
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('pub_date')[:5]
    context = {'latest_questions':latest_questions}
    return render (request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse("This is the detail view of the question: %s" % question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice= question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "Please select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def display_company(request):
    company = Company.objects.all()
    paginator = Paginator(company, 3)
    page = request.GET.get('page')
    company = paginator.get_page(page)
    context = {
        'company': company,
    }


    return render(request, 'polls/display_company.html', context)

def register_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)

        if form.is_valid():
            form.save()
            #return render(request, 'polls/index.html', {'form': form})
            return redirect('polls:index')

    else:
            form = CompanyForm()
            return render(request, 'polls/register_company.html', {'form': form})

def edit_company(request, pk):
    item = get_object_or_404(Company, pk=pk)

    if request.method == "POST":
        form = CompanyForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('polls:index')
    else:
        form = CompanyForm(instance=item)
        return render(request, 'polls/edit_company.html', {'form': form})

def delete_company(request, pk):
    Company.objects.filter(id=pk).delete()
    company = Company.objects.all()
    context = {
        'company': company,
    }
    return render(request, 'polls/display_company.html', context)

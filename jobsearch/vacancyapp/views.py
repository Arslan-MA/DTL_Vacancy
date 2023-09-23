from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from vacancyapp.utils import *
from vacancyapp.models import *
import random


def view_fucn(request):
    # Company
    # for i in range(10):
    #     Company.objects.create(name=it_companies[i])

    # Vacancy
    # for _ in range(15):
    #     VacancyTitle.objects.create(title=get_vacancy())

    # Requirements
    # for i in range(20):
    #     Requirement.objects.create(requirement=job_requirements[i])

    # for i in range(100):
    #     job = Job()
    #     job.company = random.choice(Company.objects.all())
    #     job.v_title = random.choice(VacancyTitle.objects.all())
    #     job.description = get_description()
    #     job.salary = get_salary()
    #     job.save()
    #
    #     job.requirements.set(
    #         random.sample(list(Requirement.objects.all()), k=random.randint(4, 9))
    #     )
    #
    # Job.objects.filter(company=None).delete()

    jobs = Job.objects.all()

    paginator = Paginator(jobs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj,
               "paginator": paginator}

    return render(request, "vacancyapp/vacancy_list.html", context=context)


class ViewClass(ListView):
    paginate_by = 8
    template_name = "vacancyapp/vacancy_list.html"
    model = Job

    def get_queryset(self):
        queryset = super().get_queryset()
        query_string = self.request.GET.get('q')
        if query_string:
            queryset = Job.objects.filter(
                Q(company__name__icontains=query_string) | Q(v_title__title__icontains=query_string))
        return queryset


class VacancyDetailPage(DetailView):
    model = Job
    template_name = 'vacancyapp/vacancy_detail.html'
    context_object_name = 'vacancy'


from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from api.models import Company, Vacancy
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.




def hello(request):
    return HttpResponse('Hello')

def companyIndex(request):
    companies = Company.objects.all()
    return JsonResponse(serialize('json', companies, fields=('name', 'description')), safe=False)

def companyShow(request, id):
    company = Company.objects.get(id=id)
    return JsonResponse(serialize('json', [company], fields=('name', 'description')), safe=False)

def companyVacancies(request, id):
    company = Company.objects.get(id=id)
    vacancies = Vacancy.objects.filter(company__in=[company])
    return JsonResponse(serialize('json', vacancies, fields=('name', 'description')), safe=False)


def vacancyIndex(request):
    vacancies = Vacancy.objects.all()
    return JsonResponse(serialize('json', vacancies, fields=('name', 'description', 'salary')), safe=False)

def vacancyShow(request, id):
    vacancy = Vacancy.objects.get(id=id)
    return JsonResponse(serialize('json', vacancy, fields=('name', 'description', 'salary')), safe=False)

def topVacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    return JsonResponse(serialize('json', vacancies, fields=('name', 'description', 'salary')), safe=False)



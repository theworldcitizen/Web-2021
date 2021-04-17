from django.urls import path


from api.views import *

urlpatterns = [
    path('companies', companyIndex),
    path('companies/<int:id>', companyShow),
    path('companies/<int:id>/vacancies', companyVacancies ),
    path('vacancies', vacancyIndex),
    path('vacancies/<int:id>', vacancyShow),
    path('vacancies/top_ten', topVacancies),
]
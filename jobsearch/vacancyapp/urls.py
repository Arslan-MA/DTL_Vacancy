from django.urls import path, re_path
from vacancyapp.views import *

urlpatterns = [
    # path('', view_fucn, name="func"),
    path('', ViewClass.as_view(), name="class"),
    path('vacancy_detail/<pk>', VacancyDetailPage.as_view(), name="detail")
]





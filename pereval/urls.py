from django.urls import path
from .views import PerevalList, submitData

urlpatterns = [
    path('submitData/', PerevalList.as_view(), name='pereval_list'),
    path('submitData/create/', submitData, name='submitData')
    ]
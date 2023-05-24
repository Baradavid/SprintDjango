from django.urls import path
from .views import PerevalList, submitData, getData, update_pereval

urlpatterns = [
    path('submitData/', PerevalList.as_view(), name='pereval_list'),
    path('submitData/create/', submitData, name='submitData'),
    path('submitData/<int:pk>/', getData, name='get_data'),
    path('submitData/<int:pk>/update', update_pereval, name='update_pereval'),
    ]
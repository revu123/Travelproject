from.import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),

    # path('Operation/',views.Arithmetic_operation,name='Arithmetic_opearation')
]
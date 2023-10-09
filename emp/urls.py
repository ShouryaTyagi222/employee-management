from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('add',views.add,name='add'),
    path('remove',views.remove,name='remove'),
    path('remove/<int:emp_id>',views.remove,name='remove'),
    path('all',views.all,name='all'),
    path('filter',views.filter,name='filter'),
]
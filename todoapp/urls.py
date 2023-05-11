from django.urls import path
from . import views as view 

urlpatterns=[
    path("",view.index,name="todo-index"),
    path('<int:pk>/',view.update,name="todo-update"),
    path('<int:pk>/',view.deleteTodo,name='todo-delete')
   
]
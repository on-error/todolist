from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('add', views.addTodoItem, name='add'),
      # ''' path('completed', views.completedTodo , name='completed'),'''
        path('deletecompleted', views.deletecompleted , name='deletecompleted'),
        path('deleteAll', views.deleteAll , name='deleteAll')
]

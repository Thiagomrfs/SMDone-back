from django.contrib import admin
from django.urls import path

from todos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos', ViewTodos.as_view()),
    path('todos/<int:pk>', ViewTodo.as_view())
]

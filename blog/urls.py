from django.urls import path
from .views import *

urlpatterns = [
    path('contents/', contents, name = "contents"),
    path('detail/<str:id>', detail, name = "detail"),
    path('create/', create, name = "create"),
    path('new/', new, name = "new"),
    path('edit/<str:id>', edit, name = "edit"),
    path('update/<str:id>', update, name = "update"),
    path('delete/<str:id>', delete, name = "delete"),
] 

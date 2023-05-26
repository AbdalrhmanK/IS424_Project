from django.urls import path
from . import views

urlpatterns =[
    path('add' , views.add , name='add'),
    path('home',views.home , name='home'),
     path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]
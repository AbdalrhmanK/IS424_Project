from django.urls import path
from . import views

urlpatterns =[
    path('add' , views.add , name='add'),
    path('home',views.home , name='home'),
    path('<int:product_id>' ,views.view , name="view" ),
    path('edit/<int:product_id>' ,views.edit , name="edit" ),
    path('update/<int:product_id>' ,views.update , name="update" )


]
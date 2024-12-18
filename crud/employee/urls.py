from django.urls import path
from django.urls.conf import include
from employee import views 


urlpatterns = [
    path('', views.main , name='main-page') ,
    path('emp', views.emp ,  name='add_employee'),
    path('show', views.show , name='ShowPage'), 
    path('search/', views.search_employees, name='search-employees'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('submit-vacation/<int:id>/', views.submit_vacation, name='submit_vacation'),
    path('submitted', views.submitted, name='submitted'),
    path('des/<int:id>', views.des, name='destroy_vacation'),
    path('approveVacation/<int:id>/', views.approve_vacation, name='approve_vacation'),

]
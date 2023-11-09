from django.urls import path

from todoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('classlist/',views.ListView.as_view(),name='classlist'),
    path('detaillist/<int:pk>/',views.DetailView.as_view(),name='classdetail'),
    path('updatelist/<int:pk>/',views.UpdateView.as_view(),name='classupdate'),
    path('classdelete/<int:pk>',views.DetailView.as_view(),name='classdelete'),
]
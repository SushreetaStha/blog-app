from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.BlogList.as_view(),name='home'),
    path('create/',views.BlogCreate.as_view(),name='create'),
    path('edit/<int:pk>',views.BlogUpdate.as_view(),name='edit'),
    path('delete/<int:pk>',views.BlogDelete.as_view(),name='delete')
]


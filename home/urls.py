from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('<int:detailNumber>/detail/', views.detail, name='detail'),
    path('<int:archiveNumber>/archive/', views.archive, name='archive'),
    path('comment/<int:commentNumber>/', views.comment, name='comment'),
    path('sales/', views.sales, name='sales'),
    path('rng/', views.rng, name='rng'),
    path('navbar/', views.navbar, name='navbar')
]
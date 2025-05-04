from django.urls import path
from .views import introduceView, DiaryView

urlpatterns = [
    path('introduce/', introduceView, name='introduce'),
    path('diary/', DiaryView.as_view(), name='diary'),
]

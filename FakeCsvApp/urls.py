from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('schema/', views.SchemaListViews.as_view()),
    path('schema/<int:pk>', views.SchemaDetailViews.as_view()),
]

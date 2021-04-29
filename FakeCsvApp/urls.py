from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path(
        'schema/',
        TemplateView.as_view(template_name='scheme_list.html'),
        name='schema_list'
    ),

    path('api/schema/', views.SchemaListViews.as_view(), name='schema'),
    path(
        'api/schema/<int:pk>',
        views.SchemaDetailViews.as_view(),
        name='schema_detail',
    ),
    path(
        'api/create_schema/',
        views.SchemaCreateViews.as_view(),
        name='create_schema',
    )
]

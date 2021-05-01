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
        'api/create_schema/',
        views.SchemaCreateViews.as_view(),
        name='create_schema',
    ),
    path(
        'api/schema/<int:pk>',
        views.SchemaDetailViews.as_view(),
        name='schema_detail',
    ),
    path(
        'api/schema/<int:pk>/delete',
        views.SchemaDetailViews.as_view(),
        name='delete_schema'
    ),
    path(
        'api/schema/<int:pk>/update',
        views.SchemaDetailViews.as_view(),
        name='update_schema'
    ),

    path(
        'api/create/column/',
        views.ColumnDetailView.as_view(),
        name='create_column'
    ),
    path(
        'api/column/<int:pk>/delete',
        views.ColumnDetailView.as_view(),
        name='delete_column'
    )
]

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views

urlpatterns = [
    path('api/schema/', views.SchemaListViews.as_view(), name='schema'),
    path(
        'api/create_schema/',
        views.SchemaCreateViews.as_view(),
        name='create_schema',
    ),
    path(
        'api/schema/<int:pk>/',
        views.SchemaDetailViews.as_view(),
        name='schema_detail',
    ),
    path(
        'api/schema/<int:pk>/delete/',
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
        'api/column/<int:pk>/delete/',
        views.ColumnDetailView.as_view(),
        name='delete_column'
    ),

    path(
        'api/schema/download/list/<int:pk>/',
        views.ListDownloadSchemaView.as_view(),
        name='download_list_csv'
    ),
    path(
        'api/schema/download/<int:pk>/',
        views.DetailDownloadSchemaView.as_view(),
        name='download_csv'
    ),
    path(
        'api/schema/create/csv/',
        views.CreateCsvView.as_view(),
        name='create_csv'
    ),

    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
]

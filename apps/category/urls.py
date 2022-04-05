from django.urls import path
from .views import (
    CreateCategoryApiView,
    CategoryListApiView,
    CategoryDetailApiView,
    CategoryUpdateApiView,
    CategoryDeleteApiView
)


urlpatterns = [
    path('create', CreateCategoryApiView.as_view(), name="create_category"),
    path('all', CategoryListApiView.as_view(), name="category_list"),
    path('detail/<uuid:category_id>', CategoryDetailApiView.as_view(), name="category_detail"),
    path('update/<uuid:category_id>', CategoryUpdateApiView.as_view(), name="update_category"),
    path('delete/<uuid:category_id>', CategoryDeleteApiView.as_view(), name="delete_category"),
]
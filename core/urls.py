from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path, include



schema_view = get_schema_view(
   openapi.Info(
      title="E-commerce API",
      default_version='v1',
      description="Ecommerce web app documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   authentication_classes=[]
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/users/', include("apps.users.urls")),
    path('api/v1/category/', include("apps.category.urls")),
    path('api/v1/products/', include("apps.products.urls")),
    path('api/v1/orders/', include("apps.orders.urls")),
    path('api/v1/items/', include("apps.items.urls")),
    path('api/v1/cart/', include("apps.cart.urls")),

   # drf-yasg open api
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

admin.site.site_title = "Bookr Commerce Admin"
admin.site.site_header ="Bookr Administrator"

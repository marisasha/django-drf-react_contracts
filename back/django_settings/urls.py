from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
       openapi.Info(
           title="Your API",
           default_version='v1',
           description="Description for your API",
           terms_of_service="https://www.example.com/policies/terms/",
           contact=openapi.Contact(email="marisasha228@bk.ru"),
           license=openapi.License(name="BSD License"),
       ),
       public=True,
   )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("", include("django_app.urls")),
    path("api-auth/", include("rest_framework.urls")),
]

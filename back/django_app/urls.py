from django.contrib import admin
from django.urls import path
from django_app import views
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path("api",view=views.api),
    path("api/contracts/all",view=views.api_all_contracts),
    path("api/contracts/detail/<str:id>",view=views.api_contracts_detail),
    path("api/agents",view=views.api_agents),
    path("api/agents/detail/<str:id>",view=views.api_agents_detail),
    path("api/contract/info/<str:id>",view = views.api_contract_info),
    path("api/contract/search",view = views.api_search_contract),
]

schema_view = get_schema_view(
       openapi.Info(
           title="Your API",
           default_version='v1',
           description="Description for your API",
           terms_of_service="https://www.example.com/policies/terms/",
           contact=openapi.Contact(email="contact@example.com"),
           license=openapi.License(name="BSD License"),
       ),
       public=True,
   )
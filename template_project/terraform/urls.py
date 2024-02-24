from django.urls import path
from .views import TemplateGenerateView


urlpatterns = [
    path(
        r"api/v1/template/",
        TemplateGenerateView.as_view(),
        name="template-view",
    ),
]

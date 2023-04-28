from django.urls import path

from . import views

urlpatterns = [
    path("gbp_to_usd/<int:amount>", views.gbp_to_dollar, name="gbp_to_usd"),
    path("usd_to_gbp/<int:amount>", views.usd_to_gbp, name="gbp_to_usd"),
]

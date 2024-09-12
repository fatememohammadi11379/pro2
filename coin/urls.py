from django.urls import path
from coin.views import (api_to_wallex,
                        send_email_task
)


urlpatterns = [
    path("coin/", api_to_wallex, name="coin"),
]

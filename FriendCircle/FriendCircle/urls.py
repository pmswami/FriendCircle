
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("base.urls")),
    # path('', home),
    # path('room/', room)
    path("api/", include('base.api.urls'))
]

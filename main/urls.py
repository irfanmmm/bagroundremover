from django.urls import path
from main.views import uploadimge, renderdata
from django.conf.urls.static import static
from bg import settings

app_name = "main"


urlpatterns = [
    path("", renderdata, name="renderdata"),
    path("uploadimge/", uploadimge, name="uploadimge"),

] 

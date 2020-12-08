from django.urls import path

from . import views

app_name = "core"
urlpatterns = [
    #Front Page
    path('load/<int:promptid>/',views.loadPrompt, name='loadPrompt'),
    path('', views.index, name='index'),
]

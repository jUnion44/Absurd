from django.urls import path

from . import views

app_name = "core"
urlpatterns = [
    #Front Page
    path('load/<int:promptid>/',views.loadPrompt, name='loadPrompt'),
    path('void/', views.void, name='void'),
    path('', views.index, name='index'),
]

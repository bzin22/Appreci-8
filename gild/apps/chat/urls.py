from django.urls import path
from . import views

app_name="chat"
urlpatterns = [
    path("", views.ShowChatHome, name='showchat'),
    path('<str:room_name>/<str:person_name>', views.ShowChatPage, name='showpage'),
]
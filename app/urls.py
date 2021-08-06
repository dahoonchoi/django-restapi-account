from django.urls import path
from . import views

app_name = 'app_user'
urlpatterns = [
    path('', views.DataView.as_view()),
    path('<useracct>', views.DataView.as_view())
]

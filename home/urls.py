from django.urls import path
from home.views import index
from home import views
urlpatterns = [
    path('',views.index)
]

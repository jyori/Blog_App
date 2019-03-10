from django.urls import path
from . import views
#views.home returns http response that we r on the blog page
urlpatterns = [path('', views.home, name='blog-home'),
               path('about/', views.about, name='blog-about'),
]

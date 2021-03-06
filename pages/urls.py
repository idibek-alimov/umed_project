from django.urls import path
from .views import home_page_view ,HomePageView, AboutPageView

urlpatterns = [
    #path('',HomePageView.as_view(), name='home'),
    path('',home_page_view,name='home'),
    path('about/', AboutPageView.as_view(), name='about'), # new
    path('home/', HomePageView.as_view(), name='home_page'),
]
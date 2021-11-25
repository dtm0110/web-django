from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [
   path('login/',views.login1.as_view(),name='login'),
   path('register/',views.register1.as_view(),name='register'),
   path('logout/',views.logout1,name='logout'),
]
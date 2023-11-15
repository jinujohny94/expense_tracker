from django.urls import path
from firstapp import views
app_name='firstapp'

urlpatterns= [
    path('testhtml/',views.testhtml,name='testhtml'),
    path('',views.index,name='index'),
    path('emp/',views.empDetails,name='empDetails'),
    path('signemp/',views.signemp,name='signemp')
]
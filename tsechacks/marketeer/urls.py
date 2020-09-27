from django.urls import path
from . import views



urlpatterns=[
path('mdashboard/',views.mdashboard,name="mdashboard"),

path('table/',views.table,name="table"),
path('table1/',views.table1,name="table1"),
path('sendmail/',views.sendmail,name="sendmail"),
path('sendmaile/',views.sendmaile,name="sendmaile"),

]

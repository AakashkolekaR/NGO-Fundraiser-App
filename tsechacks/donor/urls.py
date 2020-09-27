from django.urls import path
from . import views

urlpatterns=[
    path('',views.donordashboard,name='donordashboard'),
    path('donations/',views.donations,name='donations'),
    path('events/',views.donorevents,name='donorevents'),
    path('eventdesc/<str:eid>',views.eventdesc,name='eventdesc'),
    path('donorregister/',views.donorregister,name='donorregister'),
    path('login/',views.login,name='login'),
    path('registeraction/',views.registeraction,name='registeraction'),
    path('loginaction/',views.loginaction,name='loginaction'),
    path('logoutaction/',views.logoutaction,name='logoutaction'),
    path('money_donation/<str:sid>',views.money_donation,name='money_donation'),
    path('food_donation/<str:sid>',views.food_donation,name='food_donation'),
    path('stationary_donation/<str:sid>',views.stationary_donation,name='stationary_donation'),
    path('commententer',views.commententer,name='commententer'),
    path('likeadd/',views.likeadd,name='likeadd'),
    path('download_cert/<str:eid>',views.download_cert,name='download_cert'),


]

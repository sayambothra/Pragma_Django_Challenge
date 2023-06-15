from django.contrib import admin
from django.urls import path,include
from pragma_challenge import views

urlpatterns=[
    path('ApiCall/',views.OrderApiView.as_view()),
    path('Recommed/<str:product_id>/',views.RecommendProducts.as_view()),
    path('',views.index,name='index')
]
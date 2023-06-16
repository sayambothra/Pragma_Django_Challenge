from django.contrib import admin
from django.urls import path,include
from pragma_challenge import views

urlpatterns=[
    path('ApiCall/',views.OrderApiView.as_view()),#This is the path for placing an order API
    path('Recommend/<str:product_id>/',views.RecommendProducts.as_view()),# This is the path for Product Recommendations API
    path('',views.index,name='index') # This is the home page path
]
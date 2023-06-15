from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pragma_challenge import serializer
from pragma_challenge.models import Product
# Create your views here.

def index(request):
    message =" This is an Production Recommendation System"
   
    context={
        'message':message,
    }
    return render(request,'index.html',context)

#API to place an order using post method
class OrderApiView(APIView):
    serializer_class=serializer.OrdersSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            product_id = serializer.validated_data.get('productid')
            #Order_ID = serializer.validated_data.get('orderid')
            print(product_id)
            message = f'hello your order for {product_id} as been placed'            
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )


#API to get productid Recommendation based on thr productid sent to getAPI

class RecommendProducts(APIView):    
    def get(self,request,product_id):
        try:
            
            #product=request.GET.get('1RB')
            print(product_id)
            if 'B' in product_id:
                items=Product.objects.filter(product_category='badminton')
                print('Badminton')
                print(items)
            elif 'T' in product_id:
                items=Product.objects.filter(product_category='Tennis')
            item_names=[item.product_ID for item in items]

            return Response(item_names)
        except Product.DoesNotExist:
            return Response("Only this list of product_ids exist",status=404)


        


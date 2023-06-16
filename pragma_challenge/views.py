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
    '''This method helps you place orders By Selecting the product id from the dropdown.
      and gives you a confirmation message of your order'''
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data.get('productid')            
            print(product_id)
            message = f'hello your order for {product_id} as been placed'            
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )


#API to get productid Recommendation based on the productid sent to getAPI

class RecommendProducts(APIView):
    '''This is a getAPI call which helps
      to get product Recommendation based on product_id we Pass'''    
    def get(self,request,product_id):
        product_ids = Product.objects.values_list('product_ID',flat=True)
        print(list(product_ids))
        if product_id in product_ids:     
            print(product_id)
            if 'B' in product_id:
                items=Product.objects.filter(product_category='badminton')
                print('Badminton')
                
            elif 'T' in product_id:
                items=Product.objects.filter(product_category='Tennis')
            item_names=[item.product_ID for item in items]

            return Response(item_names)
        else:
            message ="product_ids =['1RB','2RB','3RB','4RB','1SB','2SB','3SB','4SB','1SSB','2SSB','3SSB','4SSB','1RT','2RT','3RT','4RT','1ST','2ST','3ST','4ST','1SST','2SST','3SST','4SST'].Only this list of product_ids exist"
            return Response(message,status=404)


        


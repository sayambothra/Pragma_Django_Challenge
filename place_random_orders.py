import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pragma2.settings')

import django
django.setup()

import random
from pragma_challenge.models import Order,Product

def random_order(N=10):
    productType =['RB','SB','SSB','RT','ST','SST']
    for i in range(1,N):   
       
        product_ids = Product.objects.values_list('product_ID',flat=True)
        random_index = random.randint(0, len(product_ids) - 1)
        random_product_id = product_ids[random_index]
        product = Product.objects.get(product_ID=random_product_id)
        print(product)
        print(random_product_id)
        order_details = Order(product_ID=product)
        order_details.save()

if __name__=='__main__':
    random_order(10)
    print('Done')



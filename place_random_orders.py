import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pragma2.settings')

import django
django.setup()

import random
from pragma_challenge.models import Order

def random_order(N=10):
    productType =['RB','SB','SSB','RT','ST','SST']
    for i in range(1,N):       
        x=random.randrange(1,5)
        y=random.randrange(0,6)
        p_ID=str(x)+productType[y]
        print(type(p_ID))        
        print(p_ID)
        order_details = Order.objects.get_or_create(product_ID=p_ID)

if __name__=='__main__':
    random_order(10)
    print('Done')



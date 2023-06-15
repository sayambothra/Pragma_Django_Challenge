import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pragma2.settings')

import django
django.setup()


from pragma_challenge.models import Product


#Script to Populate Random Prodcuts

#function to add Random badminton Racquets to the Product Model
def badmintonRacquet(N=5):
    for entry in range(1,N):
        p_ID = str(entry)+'RB'
        p_name = 'Racquet '+str(entry)
        p_category = 'badminton'
        p_price = 1000*entry

        product_details =Product.objects.get_or_create(product_ID=p_ID,product_name=p_name,product_category=p_category,product_price=p_price)


#function to add  Random badminton Shoes to the Product Model
def badmintonShoes(N=5):
    for entry in range(1,N):
        p_ID = str(entry)+'SB'
        p_name = 'Shoe '+str(entry)
        p_category = 'badminton'
        p_price = 1000*entry

        product_details =Product.objects.get_or_create(product_ID=p_ID,product_name=p_name,product_category=p_category,product_price=p_price)

#function to add  Random badminton Strings to the Product Model
def badmintonString(N=5):
    for entry in range(1,N):
        p_ID = str(entry)+'SSB'
        p_name = 'String '+str(entry)
        p_category = 'badminton'
        p_price = 100*entry

        product_details =Product.objects.get_or_create(product_ID=p_ID,product_name=p_name,product_category=p_category,product_price=p_price)
        
#function to add Random Tennis Racquets to the Product Model
def TennisRacquet(N=5):
    for entry in range(1,N):
        p_ID = str(entry)+'ST'
        p_name = 'Racquet '+str(entry)
        p_category = 'Tennis'
        p_price = 1000*entry

        product_details =Product.objects.get_or_create(product_ID=p_ID,product_name=p_name,product_category=p_category,product_price=p_price)


#function to add  Random Tennis Shoes to the Product Model
def TennisShoes(N=5):
    for entry in range(1,N):
        p_ID = str(entry)+'ST'
        p_name = 'Shoe '+str(entry)
        p_category = 'Tennis'
        p_price = 1000*entry

        product_details =Product.objects.get_or_create(product_ID=p_ID,product_name=p_name,product_category=p_category,product_price=p_price)

#function to add  Random Tennis Strings to the Product Model
def TennisString(N=5):
    for entry in range(1,N):
        p_ID = str(entry)+'SST'
        p_name = 'String '+str(entry)
        p_category = 'Tennis'
        p_price = 100*entry

        product_details =Product.objects.get_or_create(product_ID=p_ID,product_name=p_name,product_category=p_category,product_price=p_price)

if __name__ =='__main__':
    badmintonRacquet(5)
    badmintonShoes(5)
    badmintonString(5)
    TennisRacquet(5)
    TennisShoes(5)
    TennisString(5)
    print('Success')
'''Working of the Django Recommendation System'''

Step1: Pull the Project from the github link
Step2: Go to the the root folder of the project on your Commandline and:
    - pip install django
    - pip install djangorestframework

Step3 : Make the migrations in the root folder that is Pragma_Project2
        - python manage.py makemigrations pragma_challenge
        - python manage.py migrate

Step4: Deploy the Server:
       - python manage.py runserver


Step 5:
    To Execute Q1b:
    Go to populate_products.py file and just run the python file

Step 6:
    To Execute Q2b:
    Go to place_random_orders.py file and just run the python file
    
    To Execute Q2c:
        Repeat Step 4
        Go the localhosturl and after the url link type/ApiCall
        Select your product from the dropdown and clicl on POST your order will be placed
    
Step 7:
    To Execute Q3a:
    In the Product Recommendation, The logiv which I have used is if the user enters any of badminton product categories we shall display them only badminton related products and if they enter a Tennis product_id it will recommend all tennis product_ids
     Repeat Step 4
        Go the localhosturl and after the url link type/Recommend/{product_id}
            product_id = ['1RB','2RB','3RB','4RB','1SB','2SB','3SB','4SB','1SSB','2SSB','3SSB','4SSB','1RT','2RT','3RT','4RT','1ST','2ST','3ST','4ST','1SST','2SST','3SST','4SST]
        It will return the list of product_ids similar to the one you have entered.





from rest_framework import serializers

from pragma_challenge.models import Product

class ProductChoices(object):
    def __init__(self,choices):
        self.choices=choices
PC =(("Yonex Racquet","1RB"),("Lining Racquet","2RB"),("Ashaway Racquet","3RB"),("Victor Racquet ","4RB"),
     ("Yonex Shoes","1SB"),("Lining Shoes","2SB"),("Ashaway Shoes","3SB"),("Victor Shoes","4SB"),
     ("Yonex String","1SSB"),("Lining String","2SSB"),("Ashaway String","3SSB"),("Victor String","4SSB"),
     ("Wilson Racquet","1RT"),("Babolat Racquet","2RT"),("Head Racquet","3RT"),("Young Racquet","4RT"),
     ("Wilson Shoes","1ST"),("Babolat Shoes","2ST"),("Head Shoes","3ST"),("Young Shoes","4ST"),
     ("Wilson String","1SST"),("Babolat String","2SST"),("Head String","3SST"),("Young String","4SST"))

# PC =(("1RB","Yonex Racquet"),("2RB","Lining Racquet"),("3RB","Ashaway Racquet"),("4RB","Victor Racquet "),
#      ("1SB","Yonex Shoes"),("2SB","Lining Shoes"),("3SB","Ashaway Shoes",),("4SB","Victor Shoes",),
#      ("1SSB","Yonex String"),("2SSB","Lining String"),("3SSB","Ashaway String"),("4SB","Victor String","4SSB"),
#      ("1RT","Wilson Racquet"),("2RT","Babolat Racquet"),("3RT""Head Racquet"),("4SB","Young Racquet","4RT"),
#      ("1ST","Wilson Shoes"),("2ST","Babolat Shoes"),("3ST""Head Shoes","3ST"),("4SB","Young Shoes","4ST"),
#      ("1SST","Wilson String"),("2SST","Babolat String"),("3SST","Head String"),("4SB","Young String","4SST"))
class OrdersSerializer(serializers.Serializer):
    #productChoices = Product.objects.values_list('product_ID')
    orderid=serializers.CharField(max_length=10)
    productid=serializers.ChoiceField(choices=PC)
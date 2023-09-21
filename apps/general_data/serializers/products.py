from rest_framework import serializers
from ..models.products import Products, Brands

class ProductsSerializers(serializers.ModelSerializer):

      class Meta:
            model = Products
            fields = '__all__'
  
      def validate(self, data):
          print("data: ",self.initial_data)
          return data
  

class BrandsSerializers(serializers.ModelSerializer):

      class Meta:
            model = Brands
            fields = '__all__'
  
      def validate(self, data):
          print("data: ",data)
          return data
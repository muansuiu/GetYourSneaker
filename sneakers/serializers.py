from rest_framework import serializers
from .models import Brands, Products


class BrandSerializers(serializers.ModelSerializer):

    class Meta:
        model = Brands
        fields = ['name', 'country']


class ProductSerializers(serializers.ModelSerializer):
    Brand_Choice = [("", "-------")]
    Brand_Choice += [(brand.name) for brand in Brands.objects.all()]

    brand = serializers.ChoiceField(choices=Brand_Choice, required=True)
    class Meta:
        model = Products
        fields = ['name', 'brand', 'price']

    def create(self, validated_data):
        brand_name = validated_data.pop('brand')
        try:
            brand_instance = Brands.objects.get(name=brand_name)
        except Brands.DoesNotExist:
            raise serializers.ValidationError("No brand exists with this name")

        products = Products.objects.create(brand=brand_instance,  **validated_data)
        return products

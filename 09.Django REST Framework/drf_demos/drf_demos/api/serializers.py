from rest_framework import serializers

from drf_demos.api.models import Product, Category

"""
Serializers parse the model info to JSON
"""


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    # category = serializers.StringRelatedField(many=False)

    class Meta:
        model = Product
        fields = '__all__'


class IdAndNameProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')


class FullCategorySerializer(serializers.ModelSerializer):
    product_set = IdAndNameProductSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'

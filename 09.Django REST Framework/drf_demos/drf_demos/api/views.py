# from rest_framework import views as api_views
from rest_framework import generics as api_views
from rest_framework import permissions

from drf_demos.api.models import Product, Category
from drf_demos.api.serializers import ProductSerializer, FullCategorySerializer

# class ManualProductsListView(api_views.APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data, many=False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=201)
#         return Response(status=400)


'''
ListAPIView
RetrieveAPIView
CreateAPIView
UpdateAPIView
DestroyAPIView
'''


class CategoriesListView(api_views.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = FullCategorySerializer


class ProductsListView(api_views.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def list(self, request, *args, **kwargs):
        print(self.request.user)
        return super().list(request, *args, **kwargs)
    # def get_queryset(self):


class SingleProductView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# we can combine the APIViews with a Mixins

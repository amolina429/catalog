from ..serializers.products import ProductsSerializers, BrandsSerializers
from ..models.products import Products, Brands
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from ..general_functions import send_mail, html_body
from django.contrib.auth.models import User
from ..models.query_reports import QueryReports

#PRODUCTS
class ListsProductsViews(ListAPIView):
      permission_classes = [IsAuthenticated]
      queryset = Products.objects.all()
      serializer_class = ProductsSerializers

      def get(self, request, *args, **kwargs):
          return self.list(request, *args, **kwargs)
      
      def get_queryset(self):
          params = self.kwargs
          if params:
             if 'pk' in params:
                if not self.request.user.is_staff:
                   result = self.queryset.filter(pk=params['pk'])
                   if result:
                      data = result.values()[0]
                      QueryReports.objects.create(
                         product_code_fk_id=data['id'],
                         price=data['price'],
                         user_fk_id=self.request.user.id
                      )
                   return result
          return self.queryset.all()

class CreateProductsViews(CreateAPIView):
      permission_classes = [IsAuthenticated & IsAdminUser]
      serializer_class = ProductsSerializers

      def post(self, request):
          products = ProductsSerializers(data=request.data, many=True)
          if products.is_valid():
              products.save()
              return Response(products.data, status=status.HTTP_201_CREATED)
          return Response(products.errors, status=status.HTTP_400_BAD_REQUEST)

#metodos: put o patch
class UpdateProductsViews(UpdateAPIView):
      permission_classes = [IsAuthenticated & IsAdminUser]
      queryset = Products.objects.all()
      serializer_class = ProductsSerializers
      def put(self, request, *args, **kwargs):
          product = request.data['product_code']
          #consulto el correo de los usuarios que son administradores
          users_admins = User.objects.values('email').filter(is_staff=True)
          email_admins = [ users['email'] for users in users_admins]
          html_update = '''
            <div class="header">
                <h1>¡Se realizó una actualización!</h1>
            </div>
            <div class="content">
                <p>Estimado usuario,</p>
                <br>
                <p>Informamos que el producto de código %s se ha actualizado! </p>
                <br>
                <p>Gracias</p>
            </div>
          '''%(product)
          html = html_body(html_update)
          send_mail('Actualización de producto',email_admins,html)
          return self.update(request, *args, **kwargs)

      def patch(self, request, *args, **kwargs):
          #consulto el correo de los usuarios que son administradores
          product = request.data['product_code']
          users_admins = User.objects.values('email').filter(is_staff=True)
          email_admins = [ users['email'] for users in users_admins]
          html_update = '''
            <div class="header">
                <h1>¡Se realizó una actualización!</h1>
            </div>
            <div class="content">
                <p>Estimado usuario,</p>
                <br>
                <p>Informamos que el producto de código %s se ha actualizado! </p>
                <br>
                <p>Gracias</p>
            </div>
          '''%(product)
          html = html_body(html_update)
          send_mail('Actualización de producto',email_admins, html)
          return self.partial_update(request, *args, **kwargs)

class DeleteProductsViews(DestroyAPIView):
      permission_classes = [IsAuthenticated & IsAdminUser]
      queryset = Products.objects.all()
      serializer_class = ProductsSerializers
      def delete(self, request, *args, **kwargs):
          #consulto el correo de los usuarios que son administradores
          product = self.kwargs['pk']
          users_admins = User.objects.values('email').filter(is_staff=True)
          email_admins = [ users['email'] for users in users_admins]
          html_update = '''
            <div class="header">
                <h1>¡Se realizó una Eliminación de producto!</h1>
            </div>
            <div class="content">
                <p>Estimado usuario,</p>
                <br>
                <p>Informamos que el producto de id %s ha sido eliminado! </p>
                <br>
                <p>Gracias</p>
            </div>
          '''%(product)
          html = html_body(html_update)
          send_mail('Eliminación de producto',email_admins, html)
          return self.destroy(request, *args, **kwargs)

#BRANDS
class BrandsViews(CreateAPIView):
      permission_classes = [IsAuthenticated & IsAdminUser]
      serializer_class = BrandsSerializers

      def post(self, request):
          brands = BrandsSerializers(data=request.data, many=True)
          if brands.is_valid():
              brands.save()
              return Response(brands.data, status=status.HTTP_201_CREATED)
          return Response(brands.errors, status=status.HTTP_400_BAD_REQUEST)

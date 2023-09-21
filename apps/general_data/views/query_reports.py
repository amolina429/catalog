from ..serializers.query_reports import QueryReportsSerializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from ..general_functions import send_mail, html_body, generate_excel
from django.contrib.auth.models import User
from ..models.query_reports import QueryReports

#PRODUCTS
class QueryReportsViews(ListAPIView):
      permission_classes = [IsAuthenticated & IsAdminUser]
      queryset = QueryReports.objects.all()
      serializer_class = QueryReportsSerializers

      def get(self, request, *args, **kwargs):
          return self.list(request, *args, **kwargs)
      
      def get_queryset(self):
          data = self.queryset.values('id','query_date','price','product_code_fk','product_code_fk_id__name','user_fk_id__username')
          path_excel = generate_excel(data,'reporte.xlsx')
          print(path_excel)
          return self.queryset.all()
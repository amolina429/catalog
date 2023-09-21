from django.db import models
from .products import Brands, Products
from django.contrib.auth.models import User

class QueryReports(models.Model):
      query_date = models.DateTimeField('Fecha deconsulta',auto_now_add=True)
      product_code_fk = models.ForeignKey(Products, on_delete=models.PROTECT, null=False, blank=False, default='', db_column='product_code')
      price = models.DecimalField('precio del producto', max_digits=21, decimal_places=2, null=False, blank=False, default=0)
      user_fk = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, default=1, db_column='user')
  
      class Meta:
          db_table = 'query_reports'
          verbose_name = 'Informe de Consultas'
          verbose_name_plural = 'Informes de Consultas'
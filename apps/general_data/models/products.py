from django.db import models
# from . import Brand

# Create your models here.



class Brands(models.Model):
      name = models.CharField('Nombre de la marca', blank=False, max_length=100, null=False)
  
      class Meta:
          db_table = 'brand'
          verbose_name = 'Marca'
          verbose_name_plural = 'Marcas'

class Products(models.Model):
      product_code = models.CharField('Código de producto', max_length=100, unique=True)
      name = models.CharField('Nombre del producto', blank=False, max_length=100, null=False)
      price = models.DecimalField('precio del producto', max_digits=21, decimal_places=2, null=False, blank=False, default=0)
      brand_fk = models.ForeignKey(Brands, on_delete=models.PROTECT, null=False, blank=False, default=1, db_column='brand')
  
      class Meta:
          db_table = 'product'
          verbose_name = 'Producto'
          verbose_name_plural = 'Productos'
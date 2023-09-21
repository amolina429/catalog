from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User

# class UsuarioPersonalizado(AbstractUser):
#       rol = models.IntegerField("Rol para consultas", null=False, blank=False, default=1)

#       # Puedes agregar más campos si lo necesitas
#       groups = models.ManyToManyField(
#         Group,
#         verbose_name='groups',
#         blank=True,
#         related_name='usuarios_personalizados'  # Cambia 'usuarios_personalizados' a lo que prefieras
#       )
#       user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name='user permissions',
#         blank=True,
#         related_name='usuarios_personalizados_permissions'  # Cambia 'usuarios_personalizados_permissions' a lo que prefieras
#       )

#       def __str__(self):
#           return self.username

# class Rol(models.Model):
#       rol = models.CharField('Rol del usuario', max_length=10, null=False, blank=False)
#       user_fk = models.ForeignKey(User, on_delete=models.PROTECT, default=1)

#       class Meta:
#           db_table = 'rol'
#           verbose_name = 'Rol'
#           verbose_name_plural = 'Roles'
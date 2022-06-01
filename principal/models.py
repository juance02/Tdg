# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from email.policy import default
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Cabeza(models.Model):
    idcabeza = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cabeza'


class Calificaciones(models.Model):
    idcalificaciones = models.AutoField(primary_key=True)
    #perfil_idperfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='perfil_idperfil')

    class Meta:
        managed = False
        db_table = 'calificaciones'


class Categoria(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    imageulr = models.ImageField(blank=True, null=True)
    categoriaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoria'


class Comentarios(models.Model):
    idcomentarios = models.AutoField(primary_key=True)
    #perfil_idperfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='perfil_idperfil')

    class Meta:
        managed = False
        db_table = 'comentarios'


class Cotizacion(models.Model):
    idcotizacion = models.AutoField(primary_key=True)
    cuerpo_idcuerpo = models.ForeignKey('Cuerpo', models.DO_NOTHING, db_column='cuerpo_idcuerpo')
    cabeza_idcabeza = models.ForeignKey(Cabeza, models.DO_NOTHING, db_column='cabeza_idcabeza')
    kardex_idcardex = models.ForeignKey('Kardex', models.DO_NOTHING, db_column='kardex_idcardex')

    class Meta:
        managed = False
        db_table = 'cotizacion'


class Cuerpo(models.Model):
    idcuerpo = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cuerpo'


class Departamentos(models.Model):
    iddepartamentos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'departamentos'


class Entradas(models.Model):
    identradas = models.AutoField(primary_key=True)
    kardex_idcardex = models.ForeignKey('Kardex', models.DO_NOTHING, db_column='kardex_idcardex')

    class Meta:
        managed = False
        db_table = 'entradas'


class Kardex(models.Model):
    idcardex = models.AutoField(primary_key=True)
    cantidad = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'kardex'


class Municipios(models.Model):
    idmunicipios = models.IntegerField(db_column='idMunicipios', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    municipiosid = models.IntegerField(blank=True, null=True)
    departamentos_iddepartamentos = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='departamentos_iddepartamentos')

    class Meta:
        managed = False
        db_table = 'municipios'
        unique_together = (('idmunicipios', 'departamentos_iddepartamentos'),)


class Personas(models.Model):
    id_personas = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    telefono = models.BigIntegerField(blank=True, null=True)
    telefono_celular = models.BigIntegerField()
    correo_principal = models.CharField(db_column='Correo_principal', max_length=45)  # Field name made lowercase.
    correo_secundario = models.CharField(db_column='Correo_secundario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    lugar_residencia = models.CharField(max_length=45, blank=True, null=True)
    codigo_postal = models.CharField(max_length=45, blank=True, null=True)
    numero_identificacion = models.BigIntegerField()
    fecha_de_expedicion = models.DateField()
    edad = models.IntegerField()
    #personasid = models.IntegerField(blank=True, null=True)
    tipo_persona_idtipo_persona = models.ForeignKey('TipoPersona', models.DO_NOTHING, db_column='Tipo_Persona_idTipo_Persona')  # Field name made lowercase.
    departamentos_iddepartamentos = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='departamentos_iddepartamentos')
    ##perfil_idperfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='perfil_idperfil')
    cotizacion_idcotizacion = models.ForeignKey(Cotizacion, models.DO_NOTHING, db_column='cotizacion_idcotizacion')
    idtipo_de_documento_fk = models.ForeignKey('TipoDeDocumento', models.DO_NOTHING, db_column='idTipo_de_documento_fk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personas'


class Reserva(models.Model):
    idreserva = models.AutoField(primary_key=True)
    tiempo = models.DateTimeField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    class Meta:
        managed = False
        db_table = 'reserva'


class Salidas(models.Model):
    idsalidas = models.AutoField(db_column='idSalidas', primary_key=True)  # Field name made lowercase.
    kardex_idcardex = models.ForeignKey(Kardex, models.DO_NOTHING, db_column='kardex_idcardex')

    class Meta:
        managed = False
        db_table = 'salidas'


class Subcategoria(models.Model):
    idsubcategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    categoria_idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='Categoria_idCategoria')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subcategoria'


class TipoDeDocumento(models.Model):
    idtipo_de_documento = models.IntegerField(primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_de_documento'


class TipoPersona(models.Model):
    idtipo_persona = models.AutoField(db_column='idTipo_Persona', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_persona'


class UbicacionProducto(models.Model):
    idubicacion_producto = models.AutoField(db_column='idUbicacion_producto', primary_key=True)  # Field name made lowercase.
   #producto_idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_idProducto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ubicacion_producto'

class perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image =models.ImageField(default='perfil.jfif')
    descripcion = models.TextField()

    def  __str__(self):
         return f'Perfil de {self.user.username}'


class producto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product')
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()  # Field name made lowercase.
    imagen = models.ImageField()  # Field name made lowercase.
    timestamp = models.DateTimeField(default=timezone.now)
    descripcion = models.TextField()
    

    class Meta:
        ordering = ['-timestamp']

    def  __str__(self):
         return f'{self.user.username}: {self.descripcion}'

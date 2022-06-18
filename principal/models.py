# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from distutils.command import upload
from email.policy import default
from tabnanny import verbose
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


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
    idcategoria = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    #slug = AutoSlugField(populate_from='nombre')
    descripcion = models.TextField()
    image = models.ImageField(blank=True, null=True)
    #activo=models.BooleanField(default=True)
    #categoriaid = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'categoria'
        verbose_name = 'categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Categorias(models.Model):
    nombre = models.CharField(max_length=45)
    slug = AutoSlugField(populate_from='nombre')
    descripcion = models.TextField()
    image = models.ImageField(blank=True, null=True)
    activo=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name_plural='Categoria'



class Comentarios(models.Model):
    idcomentarios = models.AutoField(primary_key=True)
    #perfil_idperfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='perfil_idperfil')

    class Meta:
        managed = False
        db_table = 'comentarios'


class Cotizacion(models.Model):
    idcotizacion = models.AutoField(primary_key=True)
    cotizacion = models.CharField(max_length=100)
    cuerpo_idcuerpo = models.ForeignKey('Cuerpo', models.DO_NOTHING, db_column='cuerpo_idcuerpo')
    cabeza_idcabeza = models.ForeignKey(Cabeza, models.DO_NOTHING, db_column='cabeza_idcabeza')
    kardex_idcardex = models.ForeignKey('Kardex', models.DO_NOTHING, db_column='kardex_idcardex')

    class Meta:
        managed = False
        db_table = 'cotizacion'

    def  __str__(self):
         return f'{self.cotizacion}'


class Cuerpo(models.Model):
    idcuerpo = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cuerpo'


class Departamentos(models.Model):
    iddepartamentos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'departamentos'

    def  __str__(self):
        txt = "{0}"
        return txt.format(self.nombre)



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
    idmunicipios = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    #municipiosid = models.IntegerField(blank=True, null=True)
    departamentos_iddepartamentos = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='departamentos_iddepartamentos')

    class Meta:
        managed = False
        db_table = 'municipios'
        unique_together = (('idmunicipios', 'departamentos_iddepartamentos'),)
    
    def  __str__(self):
         return f'{self.nombre}'




   

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

class seguidores(models.Model):
    from_user = models.ForeignKey(User, related_name='califi', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='califi_to', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_user} to {self.to_user} '
    
    class Meta:
        indexes = [
        models.Index(fields=['from_user', 'to_user',]),
        ]



class TipoDeDocumento(models.Model):
    idtipo_de_documento = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_de_documento'
    
    def  __str__(self):
         return f'{self.nombre}'


class TipoPersona(models.Model):
    idtipo_persona = models.AutoField(db_column='idTipo_Persona', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_persona'
    
    def  __str__(self):
         return f'{self.nombre}'


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

    def seguir(self):
        user_ids = seguidores.objects.filter(from_user=self.user)\
                                      .values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)                              

    def dejardeseguir(self):
        user_ids = seguidores.objects.filter(to_user=self.user)\
                                      .values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids) 

class producto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product')
    nombre = models.CharField(max_length=50)
    slug=AutoSlugField(populate_from='nombre')
    categorias = models.ForeignKey(Categorias,on_delete=models.CASCADE, related_name='productoscat')
    precio = models.FloatField()  # Field name made lowercase.
    Informacion_de_produccion = models.CharField(max_length=100)
    image = models.ImageField(upload_to="productos/",null=True,blank=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(default=timezone.now)
    descripcion = models.TextField()
    destacado=models.BooleanField(default=True)
    activo=models.BooleanField(default=True)
    

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-id']

    def  __str__(self):
         return f'{self.user.username}: {self.descripcion}'
    def  __str__(self):
         return self.nombre
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Personas(models.Model):
    id_personas = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact1')
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

    def  __str__(self):
         return f'{self.nombres}'


class contacto (models.Model):
    #formper = models.ForeignKey(Personas, on_delete=models.CASCADE, related_name='contact1')
    nombre = models.CharField(max_length=50)

    def  __str__(self):
         return f'{self.formper}'




     

    
    

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cabeza(models.Model):
    idcabeza = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cabeza'


class Calificaciones(models.Model):
    idcalificaciones = models.AutoField(primary_key=True)
    perfil_idperfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='perfil_idperfil')

    class Meta:
        managed = False
        db_table = 'calificaciones'


class Categoria(models.Model):
    idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    imageulr = models.TextField(blank=True, null=True)
    categoriaid = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        txt = "{0} {1}  {2} {3}"
        return txt.format(self.idcategoria,self.nombre,self.descripcion,self.imageulr)

    class Meta:
        managed = False
        db_table = 'categoria'


class Comentarios(models.Model):
    idcomentarios = models.AutoField(primary_key=True)
    perfil_idperfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='perfil_idperfil')

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

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.iddepartamentos,self.nombre)

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

    def __str__(self):
        txt = "{0} {1} "
        return txt.format(self.idcardex,self.cantidad)

    class Meta:
        managed = False
        db_table = 'kardex'


class Municipios(models.Model):
    idmunicipios = models.IntegerField(db_column='idMunicipios', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    municipiosid = models.IntegerField(blank=True, null=True)
    departamentos_iddepartamentos = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='departamentos_iddepartamentos')

    def __str__(self):
        txt = "{0} {1} {3} "
        return txt.format(self.idmunicipios,self.nombre,self.departamentos_iddepartamentos)

    class Meta:
        managed = False
        db_table = 'municipios'
        unique_together = (('idmunicipios', 'departamentos_iddepartamentos'),)


class Perfil(models.Model):
    idperfil = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfil'


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
    personasid = models.IntegerField(blank=True, null=True)
    tipo_persona_idtipo_persona = models.ForeignKey('TipoPersona', models.DO_NOTHING, db_column='Tipo_Persona_idTipo_Persona')  # Field name made lowercase.
    departamentos_iddepartamentos = models.ForeignKey(Departamentos, models.DO_NOTHING, db_column='departamentos_iddepartamentos')
    perfil_idperfil = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='perfil_idperfil')
    cotizacion_idcotizacion = models.ForeignKey(Cotizacion, models.DO_NOTHING, db_column='cotizacion_idcotizacion')
    idtipo_de_documento_fk = models.ForeignKey('TipoDeDocumento', models.DO_NOTHING, db_column='idTipo_de_documento_fk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personas'


class Producto(models.Model):
    idproducto = models.AutoField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45)
    precio = models.FloatField(blank=True, null=True)
    productoid = models.IntegerField(blank=True, null=True)
    imagenurl = models.TextField(db_column='imagenUrl')  # Field name made lowercase.
    categoria_idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='Categoria_idCategoria')  # Field name made lowercase.
    reserva_idreserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='reserva_idreserva')
    kardex_idcardex = models.ForeignKey(Kardex, models.DO_NOTHING, db_column='kardex_idcardex')
    cotizacion_idcotizacion = models.ForeignKey(Cotizacion, models.DO_NOTHING, db_column='cotizacion_idcotizacion')

    def __str__(self):
        txt = "{0} {1} {2} {3} {5} {6} {8} "
        return txt.format(self.idproducto,self.nombre,self.descripcion,self.precio,
        self.imagenurl,self.categoria_idcategoria,self.Kardex_idcardex)

    class Meta:
        managed = False
        db_table = 'producto'


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
    
    def __str__(self):
        txt = "{0} {1} {2}"
        return txt.format(self.idsubcategoria,self.nombre,self.categoria_idcategoria)

    class Meta:
        managed = False
        db_table = 'subcategoria'


class TipoDeDocumento(models.Model):
    idtipo_de_documento = models.IntegerField(db_column='idTipo_de_documento', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.idtipo_de_documento,self.nombre)

    class Meta:
        managed = False
        db_table = 'tipo_de_documento'


class TipoPersona(models.Model):
    idtipo_persona = models.AutoField(db_column='idTipo_Persona', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.idtipo_persona,self.nombre)

    class Meta:
        managed = False
        db_table = 'tipo_persona'


class UbicacionProducto(models.Model):
    idubicacion_producto = models.AutoField(db_column='idUbicacion_producto', primary_key=True)  # Field name made lowercase.
    producto_idproducto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='Producto_idProducto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ubicacion_producto'


class User(models.Model):
    username = models.CharField(max_length=16)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=32)
    create_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        txt = "{0} {1} {2} "
        return txt.format(self.username,self.email,self.password)

    class Meta:
        managed = False
        db_table = 'user'

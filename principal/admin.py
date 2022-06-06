from django.contrib import admin
from principal.models import Cabeza
from principal.models import Comentarios
from principal.models import Calificaciones
from principal.models import Categoria
from principal.models import Cotizacion, Cuerpo
from principal.models import Departamentos
from principal.models import Entradas
from principal.models import Kardex
from principal.models import Municipios
from principal.models import perfil
from principal.models import Personas
from principal.models import Reserva
from principal.models import Salidas
from principal.models import Subcategoria
from principal.models import UbicacionProducto
from principal.models import TipoDeDocumento
from principal.models import TipoPersona
from principal.models import producto
from principal.models import contacto
#from principal.models import User
#from principal.models import UbicacionProducto


# Register your models here.

admin.site.register (Cabeza)
admin.site.register(Calificaciones)
admin.site.register(Categoria)
admin.site.register(Comentarios)
admin.site.register(Cotizacion)
admin.site.register(Cuerpo)
admin.site.register(Departamentos)
admin.site.register(Entradas)
admin.site.register(Kardex)
admin.site.register(Municipios)
admin.site.register(perfil)
admin.site.register(Personas)
admin.site.register(producto)
admin.site.register(Reserva)
admin.site.register(Salidas)
admin.site.register(Subcategoria)
admin.site.register(UbicacionProducto)
admin.site.register(TipoDeDocumento)
admin.site.register(TipoPersona)
admin.site.register(contacto)
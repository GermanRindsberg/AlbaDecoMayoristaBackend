from config.marsh import ma
from models.direccion import Direccion, Localidad, Provincia

class ProvinciaSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ('id', 'nombre','localidad_id')
        model = Provincia
provinciaSchema = ProvinciaSchema()
provinciasSchema = ProvinciaSchema(many=True)


class LocalidadSchema(ma.Schema):
    provincia=ma.Nested(ProvinciaSchema)

    class Meta:
        ordered = True
        fields = ('id', 'nombre','codigoPostal','direccion_id', 'provincia' )
        model = Localidad
localidadSchema = LocalidadSchema()
localidadesSchema = LocalidadSchema(many=True)



class DireccionSchema(ma.Schema):
    localidad= ma.Nested(LocalidadSchema)

    class Meta:
        ordered = True
        fields = ('id', 'calle', 'numero', 'piso', 'depto', 'observaciones','usuarioId', 'localidad')
        model = Direccion
direccionSchema = DireccionSchema()
direccionesSchema = DireccionSchema(many=True)
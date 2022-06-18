from config.marsh import ma
from models.perfil import Perfil


class PerfilSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ('id',
        'usuarioId',
        'nombre',
        'apellido',
        'dni',
        'cuit',
        'celular',
        'telefono'
        )
        model = Perfil

profileSchema = PerfilSchema()
profilesSchema = PerfilSchema(many=True)

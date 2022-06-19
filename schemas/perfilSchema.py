from config.marsh import ma
from models.perfil import Perfil


class PerfilSchema(ma.SQLAlchemySchema):
    class Meta:
           model=Perfil
    id=ma.auto_field()
    nombre=ma.auto_field()
    apellido = ma.auto_field()
    dni = ma.auto_field()
    cuit = ma.auto_field()
    celular =ma.auto_field()
    telefono = ma.auto_field()
    usuarioId = ma.auto_field()

perfilSchema = PerfilSchema(many=False)
perfilesSchema = PerfilSchema(many=True)

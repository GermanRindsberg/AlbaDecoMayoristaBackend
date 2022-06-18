from marshmallow import fields
from config.marsh import ma
from models.usuario import Usuario
from schemas.perfilSchema import PerfilSchema
from schemas.direccionSchema import DireccionSchema


class UsuarioSchema(ma.SQLAlchemySchema):
    perfil = ma.Nested(PerfilSchema)
    direccion= ma.Nested(DireccionSchema)
    class Meta:
        ordered = True
        fields = ('id', 'email','tipoUsuario', 'perfil', 'direccion','activo')
        #fields = ('id', 'email','activo')
        model = Usuario


class UserRegisterSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


usuarioRegisterSchema = UserRegisterSchema()
usuarioSchema = UsuarioSchema()
usuariosSchema = UsuarioSchema(many=True)

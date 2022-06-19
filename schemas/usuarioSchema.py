from marshmallow import fields
from config.marsh import ma
from models.usuario import Usuario
from schemas.direccionSchema import DireccionSchema, direccionSchema
from schemas.pedidoSchema import PedidoSchema, pedidosSchema
from schemas.perfilSchema import PerfilSchema, perfilSchema

class UsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
           model=Usuario
    id=ma.auto_field()
    email=ma.auto_field()
    tipoUsuario=ma.auto_field()
    #FORANEAS
    direccion = ma.Nested(DireccionSchema)
    perfil= ma.Nested(PerfilSchema)
    pedidos = ma.Nested(pedidosSchema)



class UserRegisterSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


usuarioRegisterSchema = UserRegisterSchema()
usuarioSchema = UsuarioSchema()
usuariosSchema = UsuarioSchema(many=True)



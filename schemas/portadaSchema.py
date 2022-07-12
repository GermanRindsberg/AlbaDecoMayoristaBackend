from config.marsh import ma
from models.portada import Portada


class PortadaSchema(ma.SQLAlchemySchema):
    class Meta:
           model=Portada
    id=ma.auto_field()
    direccionPortada=ma.auto_field()
    activo = ma.auto_field()

portadaSchema = PortadaSchema(many=False)
portadasSchema = PortadaSchema(many=True)

from config.marsh import ma
from models.foto import Foto

class FotoSchema(ma.SQLAlchemySchema):
    class Meta:
        model=Foto
    id=ma.auto_field()
    direccionImage=ma.auto_field()
    posicion=ma.auto_field()
    idProducto=ma.auto_field()
    
fotoSchema = FotoSchema()
fotosSchema = FotoSchema(many=True)



















    
 

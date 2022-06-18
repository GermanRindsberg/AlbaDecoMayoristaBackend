from config.marsh import ma
from models.categoria import Categoria

class CategoriaSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Categoria
    id = ma.auto_field()
    nombre = ma.auto_field()
    activo = ma.auto_field()

categoriaSchema = CategoriaSchema()
categoriasSchema = CategoriaSchema(many=True)

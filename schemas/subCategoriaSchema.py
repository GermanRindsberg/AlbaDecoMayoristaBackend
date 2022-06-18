
from config.marsh import ma
from models.subCategoria import SubCategoria
from schemas.categoriaSchema import CategoriaSchema


class SubCategoriaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = SubCategoria

    id = ma.auto_field()
    nombre = ma.auto_field()
    activo = ma.auto_field()
    idCategoria = ma.auto_field()
    categoria=ma.Nested(CategoriaSchema)

subCategoriaSchema = SubCategoriaSchema()
subCategoriasSchema = SubCategoriaSchema(many=True)



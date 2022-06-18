from models.producto import Producto
from config.marsh import ma
from schemas.subCategoriaSchema import subCategoriaSchema
from schemas.categoriaSchema import categoriaSchema
from schemas.varianteSchema import variantesSchema
from schemas.fotoSchema import fotosSchema


class ProductoSchema(ma.SQLAlchemySchema):
    class Meta:
        model=Producto
    id=ma.auto_field()
    nombre=ma.auto_field()
    alto=ma.auto_field()
    ancho=ma.auto_field()
    largo=ma.auto_field()
    precio=ma.auto_field()
    capacidad=ma.auto_field()
    descripcion=ma.auto_field()
    activo=ma.auto_field()
    idSubCategoria=ma.auto_field()
    idCategoria=ma.auto_field()

    subCategoria=ma.Nested(subCategoriaSchema)
    categoria=ma.Nested(categoriaSchema)
    
    variantes=ma.Nested(variantesSchema)
    fotos=ma.Nested(fotosSchema)

    
productoSchema = ProductoSchema()
productosSchema = ProductoSchema(many=True)

class ProductoSchemaParaMaestroDetalle(ma.SQLAlchemySchema):
    class Meta:
        model=Producto
    id=ma.auto_field()
    nombre=ma.auto_field()

    
productoMaestroDetalleSchema = ProductoSchemaParaMaestroDetalle()









    

from flask import request
from flask_restful import Resource
from models.categoria import Categoria
from schemas.categoriaSchema import categoriaSchema,categoriasSchema
from flask_jwt_extended import jwt_required,get_jwt_identity,verify_jwt_in_request


class CategoriaListResource(Resource):
    
    def get(self):
        categorias = Categoria.get_all_activos()
        return categoriasSchema.dump(categorias)

  
    @jwt_required()
    def post(self):
        form_data: dict = request.get_json()
        nombreCategoria=form_data.get('nombreCategoria')
        
        if Categoria.existeCategoria(nombreCategoria):
            idFam=Categoria.existeFamilia(nombreCategoria)
            categoria=Categoria.get_by_id(idFam)
            categoria.activo="activo"
            categoria.save(is_new=False)
        else:
            categoria=Categoria()
            categoria.nombre=nombreCategoria
            categoria.activo="activo"
            categoria.save(is_new=True)
        return categoriaSchema.dump(categoria), 201


class CategoriaResource(Resource):

    def get(self, id):
        categoria = Categoria.get_by_id(id)
        return categoriaSchema.dump(categoria)

    @jwt_required()
    def delete(self, id):
        categoria = Categoria.get_by_id(id)
        categoria.activo="inactivo"
        categoria.save(is_new=False)
        return 'inactivo', 204



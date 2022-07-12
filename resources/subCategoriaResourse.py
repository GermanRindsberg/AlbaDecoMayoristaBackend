from ast import Sub
from flask import request
from flask_restful import Resource
from models.subCategoria import SubCategoria
from schemas.subCategoriaSchema import subCategoriaSchema, subCategoriasSchema
from flask_jwt_extended import jwt_required,get_jwt_identity,verify_jwt_in_request


class SubCategoriaListResource(Resource):
    def get(self):
        subCategorias = SubCategoria.get_all()
        
        return subCategoriasSchema.dump(subCategorias)

    @jwt_required()
    def post(self):
        form_data: dict = request.get_json()
        nombreSubCategoria=form_data.get('nombreSubCategoria')
        idCategoria=form_data.get('idCategoria')
        idSubCategoria=SubCategoria.existeSubCategoria(nombreSubCategoria,idCategoria)
        
        if idSubCategoria!=False:
            idSubCategoria=SubCategoria.existeSubCategoria(nombreSubCategoria,idCategoria )
            subCategoria=SubCategoria.get_by_id(idSubCategoria)
            subCategoria.activo="activo"
            subCategoria.save(is_new=False)
        else:
            subCategoria=SubCategoria()
            subCategoria.nombre=nombreSubCategoria
            subCategoria.activo="activo"
            subCategoria.idCategoria=idCategoria
            subCategoria.save(is_new=True)

        return subCategoriaSchema.dump(subCategoria), 201

class SubCategoriaResource(Resource):
  
    def get(self, subCategoriaId):
        subCategoria = SubCategoria.get_by_id(subCategoriaId)
        return subCategoriasSchema(subCategoria)
        
    @jwt_required()
    def delete(self, subCategoriaId):
        subCategoria = SubCategoria.get_by_id(subCategoriaId)
        subCategoria.activo="inactivo"
        subCategoria.save(is_new=False)
        return 'inactivo', 204

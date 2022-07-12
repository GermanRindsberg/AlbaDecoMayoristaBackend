from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models.portada import Portada
from schemas.portadaSchema import portadasSchema

class PortadaListResource(Resource):
 
    def get(self):
        portadas = Portada.get_all_activos
        return portadasSchema.dump(portadas)

    @jwt_required()
    def post(self):
        portadas=request.files
        if portadas:
            for portada in portadas:
                archivoAguardar= request.files[portada]
                portada=Portada()
                portada.activo="activo"
                portada.save(is_new=True)
                portada.guardarFoto(archivoAguardar, portada.id)
        return 201


class PortadaResource(Resource):

    @jwt_required()
    def delete(self, idPortada):
        portada=Portada.get_by_id(idPortada)
        portada.activo="inactivo"
        portada.save(is_new=False)
        return 201


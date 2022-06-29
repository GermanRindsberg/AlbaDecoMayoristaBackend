from flask import Flask, json
from flask_migrate import Migrate
from flask_restful import Api
from werkzeug.exceptions import HTTPException
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config.db import db
from config.marsh import ma
from resources.subCategoriaResourse import SubCategoriaListResource, SubCategoriaResource
from resources.categoriaResource import CategoriaListResource, CategoriaResource
from resources.usuarioResourse import UserListResource, UsuarioAdmin, UsuarioResource, TokenResource
from resources.productoResource import ProductoListResource, ProductoResource
from resources.pedidoResource import PedidoListResource, PedidoResource, PedidoPorUser


app = Flask(__name__)
app.config.from_object('config.default')
CORS(app)
db.init_app(app)

ma.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)


jwt = JWTManager(app)

@app.errorhandler(HTTPException)
def handle_httpexception(e: HTTPException):
    response = e.get_response()
    response.data = json.dumps({
        'code': e.code,
        'name': e.name,
        'description': e.description
    })
    response.content_type = 'application/json'
    return response

@app.errorhandler(Exception)
def handle_exception(e: Exception):
    if isinstance(e, HTTPException):
        return e
    return {
        'code': 500,
        'name': type(e).__name__,
        'description': str(e)
    }, 500


api = Api(app)

api.add_resource(UserListResource, '/api/usuarios')
api.add_resource(UsuarioResource, '/api/usuarios/usuario/<int:idUsuario>')
api.add_resource(TokenResource, '/api/usuarios/token')
api.add_resource(UsuarioAdmin, '/api/usuarios/<int:idUsuario>')

api.add_resource(CategoriaListResource, '/api/categoria')
api.add_resource(CategoriaResource, '/api/categoria/<int:id>')

api.add_resource(SubCategoriaListResource, '/api/subCategoria')
api.add_resource(SubCategoriaResource, '/api/subCategoria/<int:subCategoriaId>')

api.add_resource(ProductoListResource, '/api/producto')
api.add_resource(ProductoResource, '/api/producto/<int:productoId>')

api.add_resource(PedidoListResource, '/api/pedido')
api.add_resource(PedidoResource, '/api/pedido/<int:idPedido>')

api.add_resource(PedidoPorUser, '/api/pedido/misPedidos/<int:idUsuario>')

if __name__ == '__main__':
     app.run(debug=False)

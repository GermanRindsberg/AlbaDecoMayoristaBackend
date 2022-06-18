from flask_jwt_extended import create_access_token
from flask import request
from flask_restful import Resource
from models.perfil import Perfil
from models.usuario import Usuario
from schemas.usuarioSchema import usuarioRegisterSchema,usuarioSchema, usuariosSchema
from models.direccion import Direccion, Localidad, Provincia


class UserListResource(Resource):
    #trae todos los usuarios
    def get(self):
        usuarios = Usuario.get_all()
        return usuariosSchema.dump(usuarios)

#guarda usuario nuevo
    def post(self):
        form_data: dict = request.get_json()

        if form_data.get('email'):
            email = form_data.get('email')
        if form_data.get('password'):
            password = form_data.get('password')

        if Usuario.email_exists(email) and password!='facebook':
             return {"errors":
                 {"msg": 'Este email ya existe en nuestra base de datos '}}
        elif Usuario.email_exists(email) and password=='facebook':
            usuario = Usuario.getByEmail(email)
            if usuario!=None:
                return usuarioSchema.dump(usuario)
            else:
                return {"errors":
                 {"msg": 'Este email ya existe en nuestra base de datos '}}
                

          
        usuario = Usuario()
        usuario.email = email
        usuario.activo="activo"
        usuario.set_password(password)
        usuario.tipoUsuario="cliente"
        usuario.save(is_new=True)


        #direccion
        direccion=Direccion()
        if form_data.get('calle'):
            direccion.calle=form_data.get('calle')
        if form_data.get('numero'):
            direccion.numero =  form_data.get('numero')
        if form_data.get('piso'):
            direccion.piso = form_data.get('piso')
        if form_data.get('depto'):
            direccion.depto = form_data.get('depto')
        if form_data.get('observacionesDomicilio'):
            direccion.observaciones = form_data.get('observacionesDomicilio')
        direccion.usuarioId=usuario.id
        direccion.save(is_new=True)

        localidad=Localidad()
        if form_data.get('localidad'):
            localidad.nombre = form_data.get('localidad')
        if form_data.get('codigoPostal'):
            localidad.codigoPostal = form_data.get('codigoPostal')
        localidad.direccion_id=direccion.id
        localidad.save(is_new=True)

        provincia=Provincia()
        if form_data.get('provincia'):
            provincia.nombre = form_data.get('provincia')
        provincia.localidad_id=localidad.id
        provincia.save(is_new=True)
                    
        perfil = Perfil()
        if form_data.get('nombre'):
            perfil.nombre = form_data.get('nombre')
        if form_data.get('apellido'):
            perfil.apellido = form_data.get('apellido')
        if form_data.get('dni'):
            perfil.dni = form_data.get('dni')
        if form_data.get('cuit'):
            perfil.cuit = form_data.get('cuit')
        if form_data.get('celular'):
            perfil.celular = form_data.get('celular')
        if form_data.get('telefono'):
            perfil.telefono = form_data.get('telefono')
        perfil.usuarioId = usuario.id  
        perfil.save(is_new=True)
   
        return usuarioSchema.dump(usuario), 201

class TokenResource(Resource):
    def post(self):
        form_data = request.get_json()
        bad_responseEmail = {"msg": "El usuario no existe"}
        bad_responsePassword = {"msg": "La contraseña es incorrecta"}
        bad_responseNoMail= {"msg": "El mail es invalido"}

        errors = usuarioRegisterSchema.validate(form_data)
        if(errors):
            return bad_responseNoMail

        email = form_data['email']
        password = form_data['password']
        
        usuario = Usuario.query.filter_by(email=email).first()

        

        if usuario is None:
            return bad_responseEmail

        
        if not usuario.check_password(password) or password=='facebook':
            return bad_responsePassword

        if usuario.activo=="inactivo":
            return bad_responseEmail

        access_token = create_access_token(identity=usuario.id)

        return {"token": access_token, "usuario": usuarioSchema.dump(usuario)}


class UsuarioResource(Resource):
    def get(self, usuarioId):
        usuario = Usuario.get_by_id(usuarioId)
        return usuarioSchema.dump(usuario)

    def patch(self, usuarioId):
        usuario = Usuario.get_by_id(usuarioId)
        form_data: dict = request.get_json()
        
        if form_data.get('password'):
            usuario.set_password(form_data.get('password'))
        if form_data.get('tipoUsuario'):
            usuario.tipoUsuario=form_data.get('tipoUsuario')
        #direccion
        if form_data.get('calle'):
            usuario.direccion.calle=form_data.get('calle')
        if form_data.get('numero'):
            usuario.direccion.numero =  form_data.get('numero')
        if form_data.get('piso'):
            usuario.direccion.piso = form_data.get('piso')
        if form_data.get('depto'):
            usuario.direccion.depto = form_data.get('depto')
        if form_data.get('observacionesDomicilio'):
            usuario.direccion.observaciones = form_data.get('observacionesDomicilio')
        if form_data.get('localidad'):
            usuario.direccion.localidad.nombre = form_data.get('localidad')
        if form_data.get('codigoPostal'):
            usuario.direccion.localidad.codigoPostal = form_data.get('codigoPostal')
        if form_data.get('provincia'):
            usuario.direccion.localidad.provincia.nombre = form_data.get('provincia')
        #perfil        
        if form_data.get('nombre'):
            usuario.perfil.nombre = form_data.get('nombre')
        if form_data.get('apellido'):
            usuario.perfil.apellido = form_data.get('apellido')
        if form_data.get('dni'):
            usuario.perfil.dni = form_data.get('dni')
        if form_data.get('cuit'):
            usuario.perfil.cuit = form_data.get('cuit')
        if form_data.get('celular'):
            usuario.perfil.celular = form_data.get('celular')
        if form_data.get('telefono'):
            usuario.perfil.telefono = form_data.get('telefono')
        usuario.save(is_new=False)
        return usuarioSchema.dump(usuario)

    def delete(self, usuarioId):
        usuario = Usuario.get_by_id(usuarioId)
        usuario.activo="inactivo"
        usuario.save(is_new=False)
        return 'inactivo', 204

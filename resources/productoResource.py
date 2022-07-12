from flask import request
from flask_restful import Resource
import json
from flask_jwt_extended import jwt_required
from models.variante import Variante
from models.foto import Foto
from models.producto import Producto
from schemas.productoSchema import productosSchema,productoSchema


class ProductoListResource(Resource):
    def get(self):
        productos = Producto.get_all_activos()
        
        return productosSchema.dump(productos)
    
    @jwt_required()
    def post(self):
        
        form_data=request.form
        fotos=request.files
        producto = Producto()
        if form_data['nombreProducto']:
            producto.nombre=form_data['nombreProducto']
        if form_data['alto']:
            producto.alto=form_data['alto']
        if form_data['ancho']:
            producto.ancho=form_data['ancho']
        if form_data['largo']:
            producto.largo=form_data['largo']
        if form_data['precio']:
            producto.precio=form_data['precio']
        if form_data['capacidad']:
            producto.capacidad=form_data['capacidad']
        if form_data['descripcion']:
            producto.descripcion=form_data['descripcion']
        producto.activo='activo'
        if form_data['idSubCategoria']:
            producto.idSubCategoria=form_data['idSubCategoria']
        if form_data['idCategoria']:
            producto.idCategoria=form_data['idCategoria']
        producto.save(is_new=True)
        #Variantes
        if form_data['variantes']:
            listaVariantes= form_data['variantes'].split(",")
            for variantes in listaVariantes:
                variante=Variante()
                variante.color=variantes
                variante.idProducto=producto.id
                variante.save(is_new=True)

        #Fotos
        if fotos:
            contador=1
            for foto in fotos:
                archivoAguardar= request.files[foto]
                foto=Foto()
                foto.posicion=contador
                foto.idProducto=producto.id
                contador+=1
                foto.save(is_new=True)
                foto.guardarFoto(archivoAguardar, foto.id)
        return productoSchema.dump(producto), 201


class ProductoResource(Resource):
    
    def get(self, productoId):
        producto = Producto.get_by_id(productoId)
        return productoSchema.dump(producto)
    @jwt_required()
    def patch(self, productoId):
        form_data=request.form
        fotos=request.files

        
        producto = Producto.get_by_id(productoId)
        if form_data['nombreProducto']:
            producto.nombre=form_data['nombreProducto']
        if form_data['alto']:
            producto.alto=form_data['alto']
        if form_data['ancho']:
            producto.ancho=form_data['ancho']
        if form_data['largo']:
            producto.largo=form_data['largo']
        if form_data['precio']:
            producto.precio=form_data['precio']
        if form_data['capacidad']:
            producto.capacidad=form_data['capacidad']
        if form_data['descripcion']:
            producto.descripcion=form_data['descripcion']
        producto.activo='activo'
        if form_data['idSubCategoria']:
            producto.idSubCategoria=form_data['idSubCategoria']
        if form_data['idCategoria']:
            producto.idCategoria=form_data['idCategoria']
        producto.save(is_new=False)


        #Variantes

        if form_data['variantes']:
            #Las variantes que vienen del front las guardo, si existe alguna en bbdd y no vienen del front las covierto en activo=0 asi no rompe Maestrodetalle
            listaVariantes= form_data['variantes'].split(",")#lista de variantes que vienen del front
            listacoloresExistentes=[]#lista de variantes que ya existen en bbdd
            for varianteExistente in producto.variantes:
                listacoloresExistentes.append(varianteExistente.color)
            listaComparada=set(listacoloresExistentes) & set(listaVariantes)
            for variante in producto.variantes:
                if variante.color not in listaComparada:
                    variante.activo=0
                    variante.save(is_new=False)
            for item in listaVariantes:
                if item not in listaComparada:
                    variante=Variante()
                    variante.idProducto=producto.id
                    variante.color=item
                    variante.activo=1
                    variante.save(is_new=True)

        #Fotos

        fotosNOborrar=[]
        if fotos:
            for foto in fotos:
                fotoAguardar=Foto()
                archivoAguardar= request.files[foto]
                fotoAguardar.idProducto=producto.id
                fotoAguardar.posicion=archivoAguardar.name
                fotoAguardar.save(is_new=True)
                fotosNOborrar.append(fotoAguardar.guardarFoto(archivoAguardar, fotoAguardar.id))
      
        data= form_data['fotosExistentes']
        fotosExistentes  = json.loads(data)
        if len(fotosExistentes)!=0:
            for elemento in fotosExistentes:
                if elemento['idImagen']!='' or elemento['idImagen']!=None:
                    fotoNOborrar=Foto.get_by_id(elemento['idImagen'])
                    fotoNOborrar.posicion=elemento['posicion']
                    fotoNOborrar.save(is_new=False)
                    fotosNOborrar.append(fotoNOborrar)

        Foto.eliminarFotosPorIdProducto(productoId,fotosNOborrar)
        return productoSchema.dump(producto), 201
  
    @jwt_required()
    def delete(self, productoId):
         producto = Producto.get_by_id(productoId)
         producto.activo="inactivo"
         producto.save(is_new=False)
         return producto.id


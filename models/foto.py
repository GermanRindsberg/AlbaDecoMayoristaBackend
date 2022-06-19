
from config.db import db, BaseModelMixin
from os import remove



class Foto(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    direccionImage = db.Column(db.String(100), unique=False)
    posicion = db.Column(db.Integer)
    # FORANEAS
    producto = db.relationship("Producto", uselist=False)
    idProducto = db.Column(db.Integer, db.ForeignKey("producto.id"), unique=False)
 

    @classmethod
    def guardarFoto(self, archivoFoto, fotoId):
        foto= self.get_by_id(fotoId)
        archivoFoto.save("backend/static/files/" + str(foto.id))
        foto.direccionImage=str(foto.id)
        foto.save(is_new=False)
        return foto

    @classmethod
    def eliminarFotosPorIdProducto(self, idProducto, listaNoBorrar):
        from models.producto import Producto
        fotos = Producto.get_by_id(idProducto).fotos
        valores=[]
        for elemento in listaNoBorrar:
                valores.append(elemento.id)
        for foto in fotos:
            if(foto.id not in valores):
                Foto.delete(foto)
                if foto.direccionImage:
                    remove("backend/static/files/"+foto.direccionImage)
        pass

    
    @classmethod
    def getAllFotosByidProducto(self, idProducto):
        from models.producto import Producto
        return Producto.get_by_id(idProducto).fotos
         
       

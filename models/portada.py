from config.db import db, BaseModelMixin

class Portada(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    direccionPortada= db.Column(db.String(100))
    activo=db.Column(db.String(10))


    @classmethod
    def guardarFoto(self, archivoFoto, idPortada):
        portada= self.get_by_id(idPortada)
        archivoFoto.save("static/portadas/" + str(portada.id))
        portada.direccionPortada=str(portada.id)
        portada.save(is_new=False)
        return portada


    

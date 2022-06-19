from config.db import db, BaseModelMixin

class Perfil(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    dni = db.Column(db.String(50))
    cuit = db.Column(db.String(50))
    celular = db.Column(db.String(30))
    telefono = db.Column(db.String(30))
    
    usuarioId = db.Column(db.Integer, db.ForeignKey("usuario.id"), unique=True, nullable=False)
    usuario = db.relationship("Usuario", back_populates="perfil")

from config.db import db, BaseModelMixin
from models.subCategoria import SubCategoria

class Categoria(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=False, nullable=False)
    activo=db.Column(db.String(10), nullable=False)
    subCategorias= db.relationship(SubCategoria, lazy='select', back_populates='categoria')
   
    @classmethod
    def existeCategoria(cls, nombre) -> bool:
        categoria = cls.query.filter_by(nombre=nombre).first()
        if not categoria:
            return False
        return categoria.id
        
  

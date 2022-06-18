from config.db import db, BaseModelMixin

class SubCategoria(db.Model, BaseModelMixin):
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre= db.Column(db.String(100), unique=False)
    activo= db.Column(db.String(100))
    categoria = db.relationship("Categoria", uselist=False)
    idCategoria = db.Column(db.Integer, db.ForeignKey("categoria.id"), unique=False, nullable=False)
    
    
    @classmethod
    def existeSubCategoria(cls, nombre, idCategoria) -> bool:
        subCat = cls.query.filter_by(nombre=nombre).first()
        if subCat !=None:
            if subCat.idCategoria==idCategoria:
                return subCat.id
            else:
                return False
        else:
            return False
    

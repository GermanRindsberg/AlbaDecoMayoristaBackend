from werkzeug.security import generate_password_hash, check_password_hash
from models.direccion import Direccion
from models.perfil import Perfil
from config.db import db, BaseModelMixin

class Usuario(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    activo=db.Column(db.String(10), nullable=False)
    tipoUsuario=db.Column(db.String(100), nullable=False)
    #FORANEAS
    perfil = db.relationship(Perfil,back_populates="usuario", uselist=False)#este
    direccion = db.relationship(Direccion, back_populates="usuario", uselist=False)


    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password) -> bool:
        return check_password_hash(self.password, password)

    @classmethod
    def email_exists(cls, email) -> bool:
        user = cls.query.filter_by(email=email).first()
        if not user:
            return False
        return True
   
    @classmethod
    def getByEmail(cls, email) -> bool:
        user = cls.query.filter_by(email=email).first()
        if not user:
            return False
        return user


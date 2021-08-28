from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import VARCHAR  # como queremos utilizar VARCHAR estamos importando un dialecto de postgres por la forma que esta estructurado Alchemy


db = SQLAlchemy()

class Account(db.Model):
    __tablename__ = 'account'
    #como hemos cambiado el nombre de la base de datos nos tenemos que ir al archivo admin.py and route.py
    #vamos a utilizar VARCHAR en la postgres almacena el tamaño del string o int en la bd
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.VARCHAR, unique=True, nullable=False)
    money = db.Column(db.Numeric, nullable=False, default=0)
    _password = db.Column(db.VARCHAR, unique=False, nullable=False) #ponemos _password para saber que es privada 
    _is_active = db.Column(db.Boolean, unique=False, nullable=False, default = True)
    ##como he cambiado las columnas necetamos hacer una migración  $pipenv run migrate
    ##tenemos la declaracion de las foreikey
    have_client = db.relationship("Client", backref="account", lazy=True) #enumeramos las realaciones con verbos(Client se refiere a la clase, account en minuscula se refierea la tabla)
    have_business = db.relationship("Business", backref="account", lazy=True) #enumeramos las realaciones con verbos(Business se refiere a la clase, account en minuscula se refierea la tabla)
    ## Con este tipo de tablas aplicamos un boolenao para decirle si es un cliente 
    is_client = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'Account{self.id}, {self.email}' #nueva formula para devolver los datos
    #transformamos toda esa información de la base de datos en un diccionario
    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "money" : self.money
            # do not serialize the password, its a security breach
        }

#La ForeignKey va en los hijos
class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.VARCHAR, unique=True, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    ## La realación con el padre
    is_account = db.relationship("Account", backref="client")

class Business(db.Model):
    __tablename__ = 'business'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.VARCHAR, unique=False, nullable=False)
    cif = db.Column(db.VARCHAR, unique=True, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id')) # no pasa nada que las dos ForeignKey se llamen igual
    ## La relacion con el padre
    is_account  = db.relationship("Account", backref="business")



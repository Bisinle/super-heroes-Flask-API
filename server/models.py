from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData



metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)
# db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'

    # serialize_rules = ('-rest_pizza_association.restaurants','pizzas',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    

    # relationship
    hero_power_association = db.relationship('HeroPower', back_populates='hero',cascade='all, delete-orphan')
    powers = association_proxy('hero_power_association','power')




    # # ---------------------------------------validations
    # @validates('name')
    # def name_validation(self, key, name):
    #     if len(name)>=50:
    #         raise ValueError('Name must be less than 50 characters')
    #     return name
    


    def __repr__(self):
        return f'(id: {self.id}, name: {self.name}. super_name: {self.super_name} )'


class HeroPower(db.Model):
    __tablename__='heropowers'

    # serialize_rules =('-pizza.rest_pizza_association', '-restaurant.rest_pizza_association',)

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)  
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    hero_id = db.Column('hero_id',db.Integer, db.ForeignKey("heroes.id"))
    power_id = db.Column('power_id',db.Integer, db.ForeignKey("powers.id"))

    hero = db.relationship('Hero', back_populates='hero_power_association')
    power = db.relationship('Power', back_populates='hero_power_association')


 

    # # ------------------------------------------validations
    # @validates('price')
    # def price_validation(self, key, price):
    #     if int(price) > 30:
    #         raise ValueError('Price must be between KSH 1 and KSH 30')
        
    #     return '$ ' + str(price)
    
    


    

    def __repr__(self):
        return f'(id: {self.id}, name: {self.strength})'



class Power(db.Model):
    __tablename__ = 'powers'


    # serialize_rules = ('-rest_pizza_association',)


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # # relationship
    hero_power_association = db.relationship('HeroPower', back_populates='power')
    heroes = association_proxy('hero_power_association','hero')


 

    def __repr__(self):
        return f'(id: {self.id}, name: {self.name}, description: {self.description}, created_at: {self.created_at})'



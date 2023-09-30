#!/usr/bin/env python3
from flask import Flask, jsonify,request,make_response,abort
from flask_restx import Api,Resource,Namespace,fields,abort
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from sqlalchemy.orm.exc import NoResultFound
# from flask_cors import CORS

from models import db, Hero,Power,HeroPower


app = Flask(__name__)
# CORS(app)
# CORS(app, origins="http://localhost:3000", supports_credentials=True, methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] =False
migrate = Migrate(app, db)

db.init_app(app)

# Instantiate Marshmallow
ma = Marshmallow(app)
'''---------------API_initialization---------------'''
api = Api()
api.init_app(app)
Hero_api=Namespace('Hero_Api')
Power_api=Namespace('Power_Api')
Hero_Power_api=Namespace('Hero_Power_api')
api.add_namespace(Hero_api)
api.add_namespace(Power_api)
api.add_namespace(Hero_Power_api)





# '''------------------------ROURCE MODELS----------------------'''
# heroes_model = api.model('Heroes',{
#     'id':fields.Integer    ,
#     'name':fields.String,
#     'super_name':fields.String,

# })


# powers_model = api.model('Powers',{
#     'id':fields.Integer    ,
#     'name':fields.String,
#     'description':fields.String,

# })    

# power_model = api.model('Power_by_id',{
#     'id':fields.Integer    ,
#     'name':fields.String,
#     'description':fields.String,
#     'heroes':fields.List(fields.Nested(heroes_model))


# })  



# hero_model = api.model('Hero_by_id',{
#     'id':fields.Integer,
#     'name':fields.String,
#     'super_name':fields.String,
#     'powers':fields.List(fields.Nested(powers_model))

# })

hero_input= api.model('post_hero',{
    'name':fields.String,
    'super_name':fields.String

})

hero_update = api.model('update_hero',{
    'super_name':fields.String
})


class PowerSchema(ma.SQLAlchemyAutoSchema):
    
    class Meta:
        model = Power
        ordered = True
        exclude = ('created_at', 'updated_at')
    
    id= ma.auto_field()
    name= ma.auto_field()
    description= ma.auto_field()
    # heroes = ma.List(ma.Nested(lambda: HeroSchema(only=('id','name','super_name'))))
    heroes = ma.List(ma.Nested('HeroSchema',only=('id','name','super_name')))




power_schema = PowerSchema()
powers_schema = PowerSchema(many =True)


class HeroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hero
        ordered = True
        exclude = ('created_at', 'updated_at')
        
    id = ma.auto_field()
    name = ma.auto_field()
    super_name = ma.auto_field()
    powers = ma.List(ma.Nested('PowerSchema',only=('id','name','description',)))


heroe_schema = HeroSchema()
heroes_schema = HeroSchema(exclude=['powers'],many=True)



'''------------------RESOURCE ROUTES-------------------------'''

@Hero_api.route('/heroes')
class Heroes(Resource):

    def get(self):      
        heroes = Hero.query.all()
        if heroes:
            return make_response(heroes_schema.dump(heroes),200)
        else:

            response =  make_response(
                {'message':'no heros in the area'}
                ,404)
            return response
     
    @Hero_api.expect(hero_input)
    def post(self):
        heroes = Hero.query.all()
        #data is in the payload
        hero = Hero(
            name= Hero_api.payload['name'],
            super_name= Hero_api.payload['super_name'],
        )
       
        if hero.super_name not in  [ h.super_name for h in heroes]:
            db.session.add(hero)
            db.session.commit()

            return make_response(heroe_schema.dump(hero),201)
        else:
            response = make_response(
                {'error':'validation error',
                 'message':'hero  super_name already exists'}
                ,404
            )

            return response




@Hero_api.route('/hero/<int:id>')
class Hero_by_id(Resource):

    def get(self,id):  
        hero = Hero.query.filter_by(id=id).first()
        if hero:
            return make_response(heroe_schema.dump(hero))
        else:
            response = make_response(
                {'error':'Hero not found, please choose another one'}
                ,404
            )

            return response
      

  



@Power_api.route('/powers')
class Powers(Resource):

    def get(self):    
        return Power.query.all(), 200


@Power_api.route('/power/<int:id>')
class Power_by_id(Resource):

    def get(self,id):        
        return Power.query.filter_by(id=id).first(), 200
    
# @Hero_Power_api.route('/hero_powers')
# class HeroPower(Resource):
#     def get(self):
#         powers = HeroPower.query.all()
     
#         return powers_schema.dump(powers), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)

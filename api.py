from flask import Flask, request
from flask_restful import Resource, Api
from model import Db

app = Flask(__name__)
api = Api(app)
db = Db()

class Agenda(Resource):
  def get(self):
    persons = db.getPersons()
    return { "success": True, "agenda": persons }
  def post(self):
    request_data = request.get_json()
    name = request_data["name"]
    phone = request_data["phone"]
    phoneType = request_data["phoneType"]
    favorite = request_data["favorite"]
    db.addPerson(name, phone, phoneType, favorite)
    return { 
            "success": True, 
            "person": { 
              "name": name, 
              "phone": phone, 
              "phoneType": phoneType, 
              "favorite": favorite 
              } 
            }

class AgendaContact(Resource):
  def get(self, id):
    return db.getPersonById(id)
  def delete(self, id):
    db.deletePerson(id)
    return { "success": True }
    

api.add_resource(Agenda, '/')
api.add_resource(AgendaContact, '/<id>')

if __name__ == '__main__':
    app.run(debug=True)
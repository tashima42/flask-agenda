from flask import Flask, request
from flask_restful import Resource, Api
from model import Db

app = Flask(__name__)
api = Api(app)
db = Db()

class Agenda(Resource):
  def get(self):
    contacts = db.getContacts()
    return { "success": True, "contacts": contacts }
  def post(self):
    request_data = request.get_json()
    name = request_data["name"]
    phone = request_data["phone"]
    phoneType = request_data["phoneType"]
    favorite = request_data["favorite"]
    db.addContact(name, phone, phoneType, favorite)
    return { 
            "success": True, 
            "contact": { 
              "name": name, 
              "phone": phone, 
              "phoneType": phoneType, 
              "favorite": favorite 
              } 
            }

class AgendaContact(Resource):
  def delete(self, id):
    db.deleteContact(id)
    return { "success": True }
    

api.add_resource(Agenda, '/agenda')
api.add_resource(AgendaContact, '/agenda/<id>')

if __name__ == '__main__':
    app.run(debug=True)
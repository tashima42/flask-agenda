from flask import Flask, request
from flask_restful import Resource, Api
from model import Db
from controller import Agenda

app = Flask(__name__)
api = Api(app)
db = Db()
agenda = Agenda()

class Contacts(Resource):
  def get(self):
    return agenda.getContacts()
  def post(self):
    request_data = request.get_json()

    name = request_data["name"]
    phone = request_data["phone"]
    phoneType = request_data["phoneType"]
    favorite = request_data["favorite"]

    agenda.addContact(name, phone, phoneType, favorite)
    return { 
            "name": name, 
            "phone": phone, 
            "phoneType": phoneType, 
            "favorite": favorite 
          }

class Contact(Resource):
  def delete(self, contact_id):
    agenda.deleteContact(contact_id)
    return { "success": True }
  def put(self, contact_id):
    request_data = request.get_json()

    name = request_data["name"]
    phone = request_data["phone"]
    phoneType = request_data["phoneType"]
    favorite = request_data["favorite"]

    agenda.updateContact(name, phone, phoneType, favorite, contact_id)
    return { 
              "id": contact_id,
              "name": name, 
              "phone": phone, 
              "phoneType": phoneType, 
              "favorite": favorite 
            }
  def get(self, contact_id):
    return agenda.getContact(contact_id)
    

api.add_resource(Contacts, '/agenda')
api.add_resource(Contact, '/agenda/<contact_id>')

if __name__ == '__main__':
    app.run(debug=True)
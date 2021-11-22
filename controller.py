from model import Db

db = Db()

class Agenda:
  def getContacts(self):
      return db.getContacts()

  def getContact(self, contact_id):
      return db.getContact(contact_id)

  def addContact(self, name, phone, phoneType, favorite):
      return db.addContact(name, phone, phoneType, favorite)

  def updateContact(self, name, phone, phoneType, favorite, contact_id):
      return db.updateContact(name, phone, phoneType, favorite, contact_id)

  def deleteContact(self, contact_id):
      return db.deleteContact(contact_id)
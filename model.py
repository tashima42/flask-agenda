import sqlite3

DATABASE = 'agenda.db'

class Db:
  def getContacts(self):
    contact =  self._query_db('SELECT * FROM contact')
    return contact
  def getContact(self, contact_id):
    contact =  self._query_db('SELECT * FROM contact WHERE id = ?', (contact_id))
    return contact
  def addContact(self, name, phone, phoneType, favorite):
    self.db.execute(
      'INSERT INTO contact (name, phone, phoneType, favorite) VALUES (?, ?, ?, ?)', 
      (name, phone, phoneType, favorite)
    )
    self.db.commit()
  def deleteContact(self, contact_id):
    self.db.execute('DELETE FROM contact WHERE id=?', (contact_id))
    self.db.commit()
  def updateContact(self, name, phone, phoneType, favorite, contact_id):
    self.db.execute(
      'UPDATE contact SET name = ?, phone = ?, phoneType = ?, favorite = ? WHERE id = ?', 
      (name, phone, phoneType, favorite, contact_id)
    )
    self.db.commit()

  def _db(self):
    db = sqlite3.connect(DATABASE, check_same_thread=False)
    db.row_factory = _make_dicts
    self.db = db  
  def _query_db(self, query, args=(), one=False):
    cur = self.db.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
  def __init__(self):
    self._db()

def _make_dicts(cursor, row):
  return dict((cursor.description[idx][0], value)
    for idx, value in enumerate(row))
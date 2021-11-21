import sqlite3
from flask import g

DATABASE = 'agenda.db'

class Db:
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

  def getPersons(self):
    persons =  self._query_db('SELECT * FROM person')
    return persons
  def getPersonById(self, person_id):
    person =  self._query_db('SELECT * FROM person WHERE id = ?', (person_id))
    return person
  def addPerson(self, name, phone, phoneType, favorite):
    self.db.execute(
      'INSERT INTO person (name, phone, phoneType, favorite) VALUES (?, ?, ?, ?)', 
      (name, phone, phoneType, favorite)
    )
    self.db.commit()
  def deletePerson(self, person_id):
    self.db.execute('DELETE FROM person WHERE id=?', (person_id))
    self.db.commit()

def _make_dicts(cursor, row):
  return dict((cursor.description[idx][0], value)
    for idx, value in enumerate(row))
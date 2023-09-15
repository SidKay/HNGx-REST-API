import db

class Person:
  def __init__(self, name, track, age):
    self.name = name
    self.track = track
    self.age = age

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': db.getid(self.name),
      'name': self.name,
      'track': self.track,
      'age':self.age
    }

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[SQLAlchemy_DATABASE_URI] = 'sqlite://database.db'

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))

class Reward(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  reward_name = db.Column(db.String(50))
  user_id = db.Column(db.Integer, primary_key=True)
  user = db.Column(db.String(50))
  #first = Reward(reward_name='Reward1', user=1)
  db.session.commit()
  #make a class in ide
  #populate the database in terminal

  @app.route('/')
  def index():
      one_user = User.query.first()
      #gives you first user in the database
      return jsonify

if __name__ == '__main__':
  app.run(debug=True)

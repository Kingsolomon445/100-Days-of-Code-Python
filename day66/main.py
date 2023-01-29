import os

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from random import choice

import json


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
    Bootstrap(app)
    return app


app = create_app()
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # This method converts the object's properties into a dictionary, which can be easily converted to JSON
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'map_url': self.map_url,
            'img_url': self.img_url,
            'location': self.location,
            'seats': self.seats,
            'has_toilet': self.has_toilet,
            'has_wifi': self.has_wifi,
            'has_sockets': self.has_sockets,
            'can_take_calls': self.can_take_calls,
            'coffee_price': self.coffee_price
        }

    # # shorter method
    # def to_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafe")
def random_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()  # or Cafe.query.all()
    cafe = choice(cafes)
    return jsonify({"cafe": cafe.to_dict()})


@app.route("/cafe/all")
def all_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify({"cafes": [cafe.to_dict() for cafe in cafes]})


@app.route("/search")
def search_cafe():
    loc = request.args.get("loc")
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    res = [cafe.to_dict() for cafe in cafes if cafe.to_dict()["location"] == loc]
    if res:
        return jsonify({"cafes": res})
    else:
        return jsonify({"error": {
            "Not Found": "Sorry, we don't have a cafe at that location."
        }})


@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(
        {
            "response": {
                "success": "Successfully added the new cafe."
            }
        }
    )


@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_coffee_price(cafe_id):
    coffee_price = request.args.get("new_price")
    if coffee_price:
        cafe = Cafe.query.filter_by(id=cafe_id).first()
        if cafe:
            cafe.coffee_price = coffee_price
            db.session.commit()
            return jsonify({"success": "Successfully updated the price."})
        else:
            return jsonify({"error": "Cafe not found."}), 404
    else:
        return jsonify({"error": "Missing new_price parameter."}), 400


@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = Cafe.query.filter_by(id=cafe_id).first()
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403



# HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)

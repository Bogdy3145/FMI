import asyncio
import json
import threading

import websockets as websockets
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'  # SQLite database file
db = SQLAlchemy(app)
connected_clients = set()


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    cookingTime = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, default=0)
    createdBy = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'name': self.name,
            'cookingTime': self.cookingTime,
            'description': self.description,
            'likes': self.likes,
            'createdBy': self.createdBy,
        }

@app.route('/')
def home():
    return render_template('index.html', message='Hello')

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    # Print the current thread ID
    print(f"Handling request in thread {threading.current_thread().ident}")

    data = request.get_json()
    new_recipe = Recipe(

        category=data['category'],
        name=data['name'],
        cookingTime=data['cookingTime'],
        description=data['description'],
        createdBy=data['createdBy']
    )

    db.session.add(new_recipe)
    db.session.commit()
    print("Recipe added successfully")
    return jsonify({'message': 'Recipe added successfully'})

@app.route('/update', methods=['PUT'])
def update_recipe():
    # Print the current thread ID
    print(f"Handling request in thread {threading.current_thread().ident}")

    data = request.get_json()
    recipe_id = data.get('id')
    recipe = Recipe.query.get(recipe_id)

    if recipe:
        # Update the recipe with the data received in the request
        recipe.category = data['category']
        recipe.name = data['name']
        recipe.cookingTime = data['cookingTime']
        recipe.description = data['description']
        recipe.likes = data['likes']
        recipe.createdBy = data['createdBy']

        db.session.commit()
        print("Recipe updated successfully")
        return jsonify({'message': 'Recipe updated successfully'})
    else:
        return jsonify({'message': 'Recipe not found'}), 404

@app.route('/recipes', methods=['GET'])
def get_all_recipes():

    # Print the current thread ID
    print(f"Handling request in thread {threading.current_thread().ident}")

    recipes = Recipe.query.all()
    recipes_list = [recipe.to_dict() for recipe in recipes]
    return jsonify({'recipes': recipes_list})

@app.route('/delete/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    # Print the current thread ID
    print(f"Handling request in thread {threading.current_thread().ident}")

    if recipe:
        db.session.delete(recipe)
        db.session.commit()
        print("Recipe deleted successfully")
        return jsonify({'message': 'Recipe deleted successfully'})
    else:
        return jsonify({'message': 'Recipe not found'}), 404




if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables before running the app



    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
    # Flash has built-in with the "threaded = True" option:
    # implementation using the SocketServer.ThreadingMixIn class

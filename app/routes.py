from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Pet

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@bp.route('/api/add_pet', methods=['POST'])
def add_pet():
    name = request.form.get('name')
    species = request.form.get('species')
    breed = request.form.get('breed')
    age = request.form.get('age')
    description = request.form.get('description')
    
    pet = Pet(name=name, species=species, breed=breed, age=age, description=description)
    db.session.add(pet)
    db.session.commit()
    
    return redirect(url_for('main.index'))

@bp.route('/delete_pet/<int:pet_id>', methods=['POST'])
def delete_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/edit_pet/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    if request.method == 'POST':
        pet.name = request.form.get('name')
        pet.species = request.form.get('species')
        pet.breed = request.form.get('breed')
        pet.age = request.form.get('age')
        pet.description = request.form.get('description')
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit_pet.html', pet=pet)

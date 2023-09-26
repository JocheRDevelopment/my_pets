import unittest
from flask import url_for
from app import create_app, db
import json
from app.models import Pet

class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()  # Manually push an application context
        self.client = self.app.test_client(use_cookies=True)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index(self):
        response = self.client.get(url_for('main.index'))
        self.assertEqual(response.status_code, 200)

    def test_add_pet(self):
        response = self.client.post(url_for('main.add_pet'), data={
            'name': 'Buddy',
            'species': 'Dog',
            'breed': 'Golden Retriever',
            'age': 3,
            'description': 'Friendly and playful'
        })
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after adding
        # Alternatively, if it returns JSON, you can do:
        # data = json.loads(response.data)
        # self.assertEqual(data['name'], 'Buddy')

    def test_edit_pet(self):
        # First, add a pet to edit
        self.client.post(url_for('main.add_pet'), data={
            'name': 'Buddy',
            'species': 'Dog',
            'breed': 'Golden Retriever',
            'age': 3,
            'description': 'Friendly and playful'
        })

        pet = Pet.query.first()
        response = self.client.post(url_for('main.edit_pet', pet_id=pet.id), data={
            'name': 'Buddy',
            'species': 'Dog',
            'breed': 'Labrador Retriever',
            'age': 3,
            'description': 'Friendly and playful'
        })
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after editing
        # Check if the pet is edited
        edited_pet = Pet.query.first()
        self.assertEqual(edited_pet.breed, 'Labrador Retriever')

    def test_delete_pet(self):
        # First, add a pet to delete
        self.client.post(url_for('main.add_pet'), data={
            'name': 'Buddy',
            'species': 'Dog',
            'breed': 'Golden Retriever',
            'age': 3,
            'description': 'Friendly and playful'
        })

        pet = Pet.query.first()
        response = self.client.post(url_for('main.delete_pet', pet_id=pet.id))
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after deleting
        # Check if the pet is deleted
        deleted_pet = Pet.query.first()
        self.assertIsNone(deleted_pet)
    


if __name__ == '__main__':
    unittest.main()

# My Pets

My Pets is a user-friendly web application developed using Flask. It provides a seamless and centralized platform for managing pet information, ideal for pet enthusiasts and shelters. The application allows users to add, update, view, and delete pet records with ease.

## Features
- **Add Pet Records:** Users can add new pets with details like name, species, breed, age, and description.
- **View Pet List:** Displays a list of all added pets with their details.
- **Update Pet Details:** Allows users to edit the information of existing pets.
- **Delete Pet Records:** Users can remove pets from the list.

## Technologies Used
- **Flask:** Lightweight WSGI web application framework.
- **SQLAlchemy:** SQL toolkit and Object-Relational Mapping (ORM) library.
- **Bootstrap:** Front-end open-source toolkit for developing with HTML, CSS, and JS.

## Setup and Installation
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/username/my-pets.git
   cd my-pets
   ```
2. **Install dependencies:**
   ```sh
   pip install Flask
   pip install Flask-SQLAlchemy
   pip install Flask-Migrate
   ```
3. **Setup DB:**
    ```sh
    export FLASK_APP=run.py
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```
4. **Run project:**
   ```sh
   python run.py
   ```
   
 ## Usage
    Navigate to http://127.0.0.1:5000/ in your web browser to start using the My Pets application.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Testing
To run the tests, execute the following command:

```sh
python test_app.py


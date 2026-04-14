from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campus_fire.db'
db = SQLAlchemy(app)

# Define User model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Define Equipment model
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Define Hazard model
class Hazard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

# Define Statistics model
class Statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_type = db.Column(db.String(50), nullable=False)
    count = db.Column(db.Integer, nullable=False)

# API Endpoint for User Registration
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'}), 201

# API Endpoint for User Authentication
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        return jsonify({'message': 'Logged in successfully!'}), 200
    return jsonify({'message': 'Invalid credentials!'}), 401

# API Endpoint for Fetching Equipment
@app.route('/api/equipment', methods=['GET'])
def get_equipment():
    equipment = Equipment.query.all()
    return jsonify([{'id': eq.id, 'name': eq.name, 'status': eq.status} for eq in equipment]), 200

# API Endpoint for Adding Equipment
@app.route('/api/equipment', methods=['POST'])
def add_equipment():
    data = request.get_json()
    new_equipment = Equipment(name=data['name'], status=data['status'])
    db.session.add(new_equipment)
    db.session.commit()
    return jsonify({'message': 'Equipment added successfully!'}), 201

# API Endpoint for Fetching Hazards
@app.route('/api/hazards', methods=['GET'])
def get_hazards():
    hazards = Hazard.query.all()
    return jsonify([{'id': h.id, 'description': h.description} for h in hazards]), 200

# API Endpoint for Adding Hazards
@app.route('/api/hazards', methods=['POST'])
def add_hazard():
    data = request.get_json()
    new_hazard = Hazard(description=data['description'])
    db.session.add(new_hazard)
    db.session.commit()
    return jsonify({'message': 'Hazard added successfully!'}), 201

# API Endpoint for Fetching Statistics
@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    statistics = Statistics.query.all()
    return jsonify([{'id': s.id, 'event_type': s.event_type, 'count': s.count} for s in statistics]), 200

# API Endpoint for Adding Statistics
@app.route('/api/statistics', methods=['POST'])
def add_statistics():
    data = request.get_json()
    new_statistic = Statistics(event_type=data['event_type'], count=data['count'])
    db.session.add(new_statistic)
    db.session.commit()
    return jsonify({'message': 'Statistics added successfully!'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
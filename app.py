from flask import Flask, jsonify, request
from services.customer_service import CustomerService
from dao.customer_dao import CustomerDAO
from db_manager import DatabaseManager
from constants import DB_CONNECTION_CONFIGURATION_FILE_PATH
from utils import load_yaml

app = Flask(__name__)

# Initialize the database manager
_db_configs = load_yaml(DB_CONNECTION_CONFIGURATION_FILE_PATH)
db_manager = DatabaseManager(host=_db_configs['server']['host'],
                             port=_db_configs['server']['port'],
                             user=_db_configs['mysql_configs']['user'],
                             password=_db_configs['mysql_configs']['password'],
                             database=_db_configs['mysql_configs']['db_name'])

# Initialize the customer DAO and service
customer_dao = CustomerDAO(db_manager)
customer_service = CustomerService(customer_dao)


# Endpoint to add a new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    try:
        data = request.get_json()
        name = data['name']
        email = data['email']
        phone = data['phone']
        address = data['address']
        customer_id = customer_service.create_customer(name, email, phone, address)
        return jsonify({'customer_id': customer_id}), 201
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid JSON data'}), 400

# Endpoint to get a customer by ID
@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = customer_service.get_customer(id)
    if customer:
        return jsonify(customer.as_dict()), 200
    else:
        return jsonify({'error': 'Customer not found'}), 404


# Endpoint to update a customer by ID
@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    try:
        data = request.get_json()
        name = data['name']
        email = data['email']
        phone = data['phone']
        address = data['address']

        customer = customer_service.update_customer(id, name, email, phone, address)
        if customer:
            return jsonify(customer.as_dict()), 202
        else:
            return jsonify({'error': 'Customer not found'}), 404
    except (KeyError, TypeError):
        return jsonify({'error': 'Invalid JSON data'}), 400


# Endpoint to delete a customer by ID
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer_id = customer_service.delete_customer(id)
    if customer_id:
        return jsonify({'customer_id': customer_id}), 200
    else:
        return jsonify({'error': 'Customer not found'}), 404


# Index
@app.route('/')
def index():
    return 'Flask Root'


if __name__ == '__main__':
    app.run(debug=True)

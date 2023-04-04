from flask import Flask, jsonify, request
from services.customer_service import CustomerService
from dao.customer_dao import CustomerDAO
from db_manager import DatabaseManager

app = Flask(__name__)

# Initialize the database manager
db_manager = DatabaseManager(host='localhost', port=3306, user='root', password='', database='car_hire_system')

# Initialize the customer DAO and service
customer_dao = CustomerDAO(db_manager)
customer_service = CustomerService(customer_dao)


# Endpoint to add a new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone']
    address = data['address']
    customer_id = customer_service.create_customer(name, email, phone, address)
    return jsonify({'customer_id': customer_id}), 201


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
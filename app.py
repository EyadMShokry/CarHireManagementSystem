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
        return jsonify(customer), 200
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
    if customer_service.update_customer(id, name, email, phone, address):
        return '', 204
    else:
        return jsonify({'error': 'Customer not found'}), 404


# Endpoint to delete a customer by ID
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    if customer_service.delete_customer(id):
        return '', 204
    else:
        return jsonify({'error': 'Customer not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)





# from flask import Flask
# from db_manager import DatabaseManager
#
# app = Flask(__name__)
#
# # Set up the database manager
# db_manager = DatabaseManager(host='localhost', port=3306, user='root', password='', database='car_hire_system')
# db_manager.init_app(app)
#
# # Create an application context
# with app.app_context():
#     # Execute a query
#     result = db_manager.execute_query("SELECT * FROM Customer")
#     print(result)
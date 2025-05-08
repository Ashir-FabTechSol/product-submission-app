import os
from flask import Flask, request, jsonify, render_template
from Models.models import db, Product
from config import Config


def create_db_directory():
    if not os.path.exists('Database'):
        os.makedirs('Database')

# Initialize Flask app and database
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Create the Database directory
create_db_directory()

# Initialize database
def init_db():
    with app.app_context():
        db.create_all()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.order_by(Product.created_at.desc()).all()
        return jsonify([product.to_dict() for product in products])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/products', methods=['POST'])
def add_product():
    try:
        data = request.json
        name = data.get('name', '').strip()
        price = data.get('price')
        description = data.get('description', '').strip()

        if not name or not price:
            return jsonify({'error': 'Name and price are required'}), 400

        if not isinstance(price, (int, float)) or price <= 0:
            return jsonify({'error': 'Price must be a positive number'}), 400

        product = Product(name=name, price=price, description=description)
        db.session.add(product)
        db.session.commit()

        return jsonify({'message': 'Product added successfully', 'product': product.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    init_db()
    app.run(debug=True)

























# import os
# from flask import Flask, request, jsonify, render_template
# from Database.models import db, Product

# # Create Database directory if it doesn't exist — move this block **above** all db usage
# if not os.path.exists('Database'):
#     os.makedirs('Database')

# class Config:
#     basedir = os.path.abspath(os.path.dirname(__file__))
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change'
#     SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'Database', 'products.db')}"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# app = Flask(__name__)
# app.config.from_object(Config)
# db.init_app(app)


# def init_db():
#     with app.app_context():
#         db.create_all()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/api/products', methods=['GET'])
# def get_products():
#     try:
#         products = Product.query.order_by(Product.created_at.desc()).all()
#         return jsonify([product.to_dict() for product in products])
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @app.route('/api/products', methods=['POST'])
# def add_product():
#     try:
#         data = request.json
#         name = data.get('name', '').strip()
#         price = data.get('price')
#         description = data.get('description', '').strip()
        
#         if not name or not price:
#             return jsonify({'error': 'Name and price are required'}), 400
        
#         if not isinstance(price, (int, float)) or price <= 0:
#             return jsonify({'error': 'Price must be a positive number'}), 400
        
#         product = Product(name=name, price=price, description=description)
#         db.session.add(product)
#         db.session.commit()
        
#         return jsonify({'message': 'Product added successfully', 'product': product.to_dict()}), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     init_db()
#     app.run(debug=True)




























# from flask import Flask, request, jsonify, render_template
# from Database.models import db, Product
# from config import Config
# import os

# app = Flask(__name__)
# app.config.from_object(Config)
# db.init_app(app)

# # Create Database directory if it doesn't exist
# if not os.path.exists('Database'):
#     os.makedirs('Database')

# def init_db():
#     with app.app_context():
#         db.create_all()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/api/products', methods=['GET'])
# def get_products():
#     try:
#         products = Product.query.order_by(Product.created_at.desc()).all()
#         return jsonify([product.to_dict() for product in products])
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @app.route('/api/products', methods=['POST'])
# def add_product():
#     try:
#         data = request.json
#         name = data.get('name', '').strip()
#         price = data.get('price')
#         description = data.get('description', '').strip()
        
#         if not name or not price:
#             return jsonify({'error': 'Name and price are required'}), 400
        
#         if not isinstance(price, (int, float)) or price <= 0:
#             return jsonify({'error': 'Price must be a positive number'}), 400
        
#         product = Product(name=name, price=price, description=description)
#         db.session.add(product)
#         db.session.commit()
        
#         return jsonify({'message': 'Product added successfully', 'product': product.to_dict()}), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     init_db()
#     app.run(debug=True) 
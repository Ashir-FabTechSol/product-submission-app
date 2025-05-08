import os

class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'Database', 'products.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False



















# # config.py
# import os

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change'
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///Database/products.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# Mini Product Submission App

A lightweight Flask web application for managing products. Users can add products with names, prices, and descriptions, and view the list of submitted products.

## Features

- Add new products with name, price, and description
- View list of all products
- Form validation
- Responsive design
- SQLite database for data persistence

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository or download the source code

2. Create a virtual environment (recommended):
```bash
python -m venv myenv
```

3. Activate the virtual environment:
- On Windows:
```bash
myenv\Scripts\activate
```
- On macOS/Linux:
```bash
source myenv/bin/activate
```

4. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Make sure your virtual environment is activated

2. Run the Flask application:
```bash
python app.py
```

3. Open your web browser and navigate to:


## API Endpoints

- `GET /api/products`: Retrieve all products
- `POST /api/products`: Add a new product
  - Required fields: name, price
  - Optional fields: description

## Database

The application uses SQLite as its database. The database file (`products.db`) is created automatically when you first run the application.

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.

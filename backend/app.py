from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import os

app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde el frontend

# Configuración de MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://oop:oop@cluster0.9knxc.mongodb.net/?appName=Cluster0")
DATABASE_NAME = "oop"
COLLECTION_NAME = "Customers"

# Conexión a MongoDB
try:
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    print("✅ Conexión exitosa a MongoDB")
except Exception as e:
    print(f" Error al conectar con MongoDB: {e}")

# Ruta principal
@app.route('/')
def home():
    return jsonify({
        "message": "API REST de Customers",
        "endpoints": {
            "/api/customers": "GET - Obtener todos los clientes"
        }
    })

# Endpoint GET para obtener todos los clientes
@app.route('/api/customers', methods=['GET'])
def get_customers():
    try:
        # Obtener todos los documentos de la colección
        customers = list(collection.find())
        
        # Convertir ObjectId a string para JSON
        for customer in customers:
            customer['_id'] = str(customer['_id'])
        
        return jsonify({
            "success": True,
            "count": len(customers),
            "data": customers
        }), 200
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

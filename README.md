# 🏪 Sistema de Gestión de Clientes - MongoDB

Aplicación completa con backend en Python (Flask) y frontend en HTML/CSS/JavaScript para visualizar clientes desde MongoDB.

## 📁 Estructura del Proyecto

```
ServicioRestPython/
├── backend/
│   ├── app.py                 # API REST con Flask
│   ├── requirements.txt       # Dependencias Python
│   ├── .env.example          # Ejemplo de variables de entorno
│   └── README.md             # Documentación del backend
├── frontend/
│   ├── index.html            # Interfaz de usuario
│   └── README.md             # Documentación del frontend
└── README.md                 # Este archivo
```

## 🚀 Inicio Rápido

### 1. Configurar Backend

```bash
# Navegar al directorio backend
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# ⚠️ IMPORTANTE: Editar app.py y reemplazar <db_password> con tu contraseña real

# Ejecutar el servidor
python app.py
```

El backend estará disponible en: `http://localhost:5000`

### 2. Configurar Frontend

```bash
# En otra terminal, navegar al directorio frontend
cd frontend

# Opción 1: Abrir directamente
# Abre index.html en tu navegador

# Opción 2: Servidor local (recomendado)
python -m http.server 8000
```

El frontend estará disponible en: `http://localhost:8000`

## 🔑 Configuración de MongoDB

**⚠️ IMPORTANTE:** Antes de ejecutar, debes reemplazar `<db_password>` en `backend/app.py` (línea 11) con tu contraseña real de MongoDB:

```python
MONGO_URI = "mongodb+srv://oop:TU_CONTRASEÑA_AQUI@cluster0.9knxc.mongodb.net/?appName=Cluster0"
```

## 📡 API Endpoints

### GET `/`
Información de la API

**Respuesta:**
```json
{
  "message": "API REST de Customers",
  "endpoints": {
    "/api/customers": "GET - Obtener todos los clientes"
  }
}
```

### GET `/api/customers`
Obtiene todos los clientes de la base de datos

**Respuesta exitosa:**
```json
{
  "success": true,
  "count": 2,
  "data": [
    {
      "_id": "62d0ea3866004ac95439cce4",
      "id": 2,
      "fullName": "Jorge Lascano",
      "email": "jorge_lascano@yahoo.com",
      "type": "Frquent",
      "discount": 5,
      "totalSale": 20
    }
  ]
}
```

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.x**
- **Flask** - Framework web
- **Flask-CORS** - Manejo de CORS
- **PyMongo** - Driver de MongoDB
- **DNSPython** - Resolución DNS para MongoDB Atlas

### Frontend
- **HTML5**
- **CSS3** (Vanilla, sin frameworks)
- **JavaScript** (Vanilla, Fetch API)

## ✨ Características

### Backend
- ✅ API RESTful con Flask
- ✅ Conexión a MongoDB Atlas
- ✅ CORS habilitado para desarrollo
- ✅ Manejo de errores
- ✅ Conversión automática de ObjectId a string

### Frontend
- ✅ Diseño moderno y responsivo
- ✅ Tabla con datos en tiempo real
- ✅ Indicador de estado de conexión
- ✅ Botón de actualización manual
- ✅ Contador de clientes
- ✅ Badges de tipo de cliente con colores
- ✅ Animaciones y efectos hover
- ✅ Loading spinner
- ✅ Manejo de errores con mensajes descriptivos

## 🔧 Solución de Problemas

### Error de conexión a MongoDB
- Verifica que tu contraseña esté correctamente configurada
- Asegúrate de que tu IP esté en la lista blanca de MongoDB Atlas
- Verifica la conectividad a internet

### Error de CORS
- Asegúrate de que el backend esté ejecutándose
- Verifica que Flask-CORS esté instalado: `pip install flask-cors`

### La tabla no muestra datos
- Verifica que el backend esté ejecutándose en `http://localhost:5000`
- Abre la consola del navegador (F12) para ver errores
- Verifica que haya datos en la colección MongoDB

## 📝 Notas

- El backend utiliza el puerto **5000**
- El frontend puede ejecutarse en cualquier puerto (recomendado: 8000)
- Los servicios están completamente desacoplados
- No se requiere compilación ni build para el frontend

## 🔐 Seguridad

⚠️ **Para producción:**
- Usar variables de entorno para credenciales
- Implementar autenticación y autorización
- Configurar CORS apropiadamente
- Usar HTTPS
- Validar y sanitizar datos de entrada

## 📄 Licencia

Este proyecto es de uso libre para fines educativos.

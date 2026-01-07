# Backend - API REST con Python y Flask

## Instalación

1. Crear un entorno virtual:
```bash
python -m venv venv
```

2. Activar el entorno virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. **Importante**: Reemplaza `<db_password>` en `app.py` con tu contraseña real de MongoDB

## Ejecución

```bash
python app.py
```

El servidor estará disponible en: `http://localhost:5000`

## Endpoints

- `GET /` - Información de la API
- `GET /api/customers` - Obtener todos los clientes

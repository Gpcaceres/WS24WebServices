# Frontend - Visualización de Clientes

## Descripción

Frontend simple con HTML, CSS y JavaScript vanilla para mostrar los clientes de MongoDB en una tabla.

## Ejecución

### Opción 1: Abrir directamente el archivo
Simplemente abre `index.html` en tu navegador

### Opción 2: Servidor local (recomendado)

#### Con Python:
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

#### Con Node.js:
```bash
npx http-server -p 8000
```

#### Con Live Server (VS Code):
1. Instala la extensión "Live Server"
2. Click derecho en `index.html` → "Open with Live Server"

Luego accede a: `http://localhost:8000`

## Características

- ✅ Tabla responsiva con diseño moderno
- ✅ Actualización automática de datos
- ✅ Indicador de estado de conexión
- ✅ Contador de clientes
- ✅ Badges de tipo de cliente con colores
- ✅ Efectos hover y animaciones
- ✅ Manejo de errores
- ✅ Loading spinner

## Requisitos

- El backend debe estar ejecutándose en `http://localhost:5000`
- Navegador moderno con soporte para Fetch API

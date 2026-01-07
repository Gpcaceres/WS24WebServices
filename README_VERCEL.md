# 🚀 Guía de Despliegue en Vercel

## Pasos para desplegar:

### 1. Preparar el repositorio
```bash
git add .
git commit -m "Preparar proyecto para Vercel"
git push origin main
```

### 2. Configurar en Vercel

1. Ve a [vercel.com](https://vercel.com) e inicia sesión con GitHub
2. Haz clic en "Add New Project"
3. Importa el repositorio `WS24WebServices`
4. Vercel detectará automáticamente la configuración

### 3. Configurar Variables de Entorno

En la sección de configuración del proyecto en Vercel:
- Ve a "Settings" → "Environment Variables"
- Agrega la variable:
  - **Name:** `MONGO_URI`
  - **Value:** `mongodb+srv://oop:oop@cluster0.9knxc.mongodb.net/?appName=Cluster0`

### 4. Desplegar

Haz clic en "Deploy" y espera a que Vercel complete el despliegue.

## 📝 Notas Importantes

- El frontend estará disponible en: `https://tu-proyecto.vercel.app/`
- La API estará disponible en: `https://tu-proyecto.vercel.app/api/customers`
- Vercel actualizará automáticamente el proyecto con cada push a `main`

## 🔄 Actualizar el frontend

Si el frontend hace peticiones a `localhost`, actualiza la URL a tu dominio de Vercel:

```javascript
const API_URL = 'https://tu-proyecto.vercel.app/api/customers';
```

## 🔒 Seguridad

⚠️ **IMPORTANTE:** La URI de MongoDB está hardcodeada. Para producción:
1. Cambia las credenciales de MongoDB
2. Usa variables de entorno en Vercel
3. Restringe el acceso por IP en MongoDB Atlas

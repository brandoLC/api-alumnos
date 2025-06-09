# API de Alumnos - Serverless

Este proyecto implementa una API RESTful para la gestión de alumnos utilizando AWS Lambda, API Gateway y DynamoDB.

## Estructura del Proyecto

```
├── CrearAlumno.py          # Función Lambda para crear alumnos
├── ListarAlumnos.py        # Función Lambda para listar alumnos
├── ObtenerAlumno.py        # Función Lambda para obtener un alumno específico
├── ActualizarAlumno.py     # Función Lambda para actualizar alumnos
├── EliminarAlumno.py       # Función Lambda para eliminar alumnos
├── serverless.yml          # Configuración de Serverless Framework
├── requirements.txt        # Dependencias de Python
└── README.md              # Este archivo
```

## Funcionalidades

### 1. Crear Alumno (POST)
- **Endpoint**: `/alumnos/crear`
- **Método**: POST
- **Body**:
```json
{
  "tenant_id": "string",
  "alumno_id": "string",
  "alumno_datos": {
    "nombre": "string",
    "email": "string",
    "edad": "number"
  }
}
```

### 2. Listar Alumnos (POST)
- **Endpoint**: `/alumnos/listar`
- **Método**: POST
- **Body**:
```json
{
  "tenant_id": "string"
}
```

### 3. Obtener Alumno (POST)
- **Endpoint**: `/alumnos/obtener`
- **Método**: POST
- **Body**:
```json
{
  "tenant_id": "string",
  "alumno_id": "string"
}
```

### 4. Actualizar Alumno (POST)
- **Endpoint**: `/alumnos/actualizar`
- **Método**: POST
- **Body**:
```json
{
  "tenant_id": "string",
  "alumno_id": "string",
  "alumno_datos": {
    "nombre": "string",
    "email": "string",
    "edad": "number"
  }
}
```

### 5. Eliminar Alumno (POST)
- **Endpoint**: `/alumnos/eliminar`
- **Método**: POST
- **Body**:
```json
{
  "tenant_id": "string",
  "alumno_id": "string"
}
```

## Tabla DynamoDB

- **Nombre**: `t_alumnos`
- **Partition Key**: `tenant_id` (String)
- **Sort Key**: `alumno_id` (String)
- **Billing Mode**: Pay per request

## Despliegue

### Requisitos previos
1. Node.js instalado
2. Serverless Framework instalado
3. Credenciales de AWS configuradas

### Instalación
```bash
npm install -g serverless
```

### Despliegue
```bash
serverless deploy
```

### Eliminar el stack
```bash
serverless remove
```

## Códigos de Estado HTTP

- **200**: Operación exitosa
- **201**: Recurso creado exitosamente
- **400**: Solicitud incorrecta (parámetros faltantes o incorrectos)
- **404**: Recurso no encontrado
- **409**: Conflicto (el recurso ya existe)
- **500**: Error interno del servidor

## Estructura de Respuesta

Todas las respuestas siguen el siguiente formato:
```json
{
  "statusCode": 200,
  "body": "{\"message\":\"Operación exitosa\", \"data\": {}}"
}
```

## Notas
- Todas las respuestas están en formato JSON
- Los errores incluyen mensajes descriptivos
- Se incluye logging para facilitar el debugging
- CORS está habilitado para todas las funciones

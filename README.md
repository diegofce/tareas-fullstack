// ...existing code...
# Sistema de Gestión de Tareas – Prueba Técnica

Aplicación full-stack ligera, construida con Django + DjangoRestFramework (renderizado por servidor). Esta copia refleja la estructura real del proyecto en esta carpeta.

---

## Resumen rápido

Aplicación full-stack construida utilizando:

- **Backend:** Django REST Framework + JWT Authentication  
- **Frontend:** Vue 3 + Vite  
- **Base de datos:** PostgreSQL  
- **Autenticación:** SimpleJWT  
- **Extras:** Filtros, CRUD, rutas protegidas.

---

## 🚀 Funcionalidades

### Backend (Django)
- Registro de usuarios
- Login con JWT (access + refresh)
- Endpoints protegidos
- CRUD completo de tareas
- Filtros: pendientes / completada

### Frontend (Vue)
- Login
- Registro
- Listado de tareas
- Tareas completadas / pendientes
- Vista de detalle de tarea
- Crear / actualizar / finalizar / eliminar
- Manejo automático de token con Axios Interceptors

## 🛠 Tecnologías

| Área | Tecnología |
|------|------------|
| Backend | Python, Django, DRF, SimpleJWT |
| Frontend | Vue 3, Vite, Axios |
| Base de datos | PostgreSQL |

## Requisitos (recomendado)
- Python 3.10+ (usar la misma versión del venv)  
- pip  
- Virtualenv (opcional si ya existe `venv/`)  

pip install -r requirements.txt
# o (si no hay requirements)
pip install django
```

---

## Configuración y ejecución (Windows - PowerShell)

1. Activar entorno virtual:
```.\venv\Scripts\Activate.ps1
```

2. Aplicar migraciones:
```
python manage.py migrate
```

3. Crear superusuario (opcional):
```
python manage.py createsuperuser
```

4. Correr servidor de desarrollo:
```
python manage.py runserver
```
---
## 📝 README.md - API de Tareas

Este documento describe los **endpoints principales** para la interacción con la API de Tareas, incluyendo los flujos de autenticación y la gestión de tareas.

---

### 🔑 Autenticación


| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| **POST** | `/api/register/` | Crea un **nuevo usuario** en el sistema. |
| **POST** | `/api/token/` | Permite el **inicio de sesión** (Login) y la obtención de los tokens de acceso y refresco. |
| **POST** | `/api/token/refresh/` | Utiliza el token de refresco para obtener un **nuevo token de acceso**. |

---

### ✅ Tareas (Tasks)

Estos endpoints permiten la **gestión completa de las tareas** (CRUD - Crear, Leer, Actualizar, Eliminar). Para acceder a ellos, se requiere un **token de autenticación** válido.

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| **GET** | `/api/tasks/` | **Lista** todas las tareas del usuario autenticado. |
| **POST** | `/api/tasks/` | **Crea una nueva tarea**. |
| **GET** | `/api/tasks/:id/` | **Ver el detalle** de una tarea específica, usando su `:id`. |
| **PUT** | `/api/tasks/:id/` | **Actualiza** completamente todos los campos de una tarea específica. |
| **PATCH** | `/api/tasks/:id/` | **Marca una tarea como completada** (o realiza una actualización parcial). |
| **DELETE** | `/api/tasks/:id/** | **Elimina** una tarea específica. |

## Autor
Prueba técnica desarrollada por [DIEGO F CHACON] 
Visita: [(diegof.netlify.app)]

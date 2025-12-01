# REQUIREMENTS_AND_DESIGN

## Proyecto

**Nombre:** Plataforma de gestión de tareas (backend Django + DRF, frontend Vue 3)

**Autor:** Diego Chacón

**Descripción breve:** API REST en Django para registro y gestión de tareas personales (CRUD), con frontend en Vue 3 que consume la API y usa JWT para autenticación.

---

## 1. Requerimientos funcionales

1. Registro de usuario (endpoint público).
2. Autenticación JWT (token de acceso y refresh).
3. CRUD de tareas (crear, listar, obtener, actualizar, eliminar) para usuarios autenticados.
4. Cada usuario solo ve/edita/elimina sus propias tareas.
5. Campos de Task: `title` (required), `description` (optional), `created` (timestamp), `date_completed` (nullable), `important` (boolean), `user` (FK).

## 2. Requerimientos no funcionales

* Seguridad: JWT, permisos por objeto.
* Base de datos: PostgreSQL.
* Documentación y README con pasos para correr local y deployment (Render backend, Vercel frontend).
* Commits significativos en GitHub.

## 3. Supuestos

* Usuarios se identifican con `usuario` y `contraseña`.
* El frontend y backend son proyectos separados en el mismo repo (carpetas `/backend` y `/frontend`).
* El backend expone ruta base `/api/`.

## 4. ERD (modelo de datos)

* **User** (Django `auth_user`)

  * id, username, password

* **Task**

  * id (PK)
  * title (string, required)
  * description (text, optional)
  * created (datetime)
  * date_completed (datetime, null)
  * important (boolean)
  * user_id (FK → auth_user.id)

*(Ver ERD gráfico incluido en el PDF adjunto)*

## 5. Endpoints implementados

Base URL: `/api/`

* `POST /api/register/` — Registrar usuario (público). Request: `{username, password}`. 
* `POST /api/token/` — Obtener tokens (access, refresh). Request: `{username, password}`.
* `POST /api/refresh/` — Refresh token.
* `GET /api/tasks/` — Listar tareas del usuario autenticado.
* `POST /api/tasks/` — Crear tarea para usuario autenticado.
* `GET /api/tasks/{id}/` — Obtener detalle (solo propietario).
* `PATCH /api/tasks/{id}/` — Actualizar campos (solo propietario).
* `PUT /api/tasks/{id}/` — Reemplazar (opcional) (solo propietario).
* `DELETE /api/tasks/{id}/` — Eliminar (solo propietario).

## 6. Flujo de autenticación JWT

1. Registro → `/api/register/` (público).
2. Login → `/api/token/` retorna `access` y `refresh`.
3. Frontend guarda tokens en `localStorage`.
4. Cada request autenticado añade header `Authorization: Bearer <access>`.
5. Cuando access expira, usar `/api/refresh/` para obtener nuevo access.

*Diagrama de flujo 

## 7. Seguridad y permisos

* `DEFAULT_PERMISSION_CLASSES` en DRF: `IsAuthenticated` por defecto.
* Permisos por objeto: validar `task.user == request.user` para update/delete.
* HTTPS en producción 

## 8. Despliegue

**Backend (Render):**

* Variables de entorno: `SECRET_KEY`, `DEBUG=False`, `DATABASE_URL`, `ALLOWED_HOSTS`
* Comandos de build: `pip install -r requirements.txt`.
* Start command: `gunicorn tareas.wsgi`.
* Ejecutar migraciones: `python manage.py migrate` 

**Frontend (Vercel):**

* `VITE_API_URL` → apuntar al backend `https://tareas-fullstack.onrender.com/api`
* Build command: `npm run build` (Vite) y output `dist`.

## 9. Estructura del repositorio

```
/ (repo root)
  /backend (Django project `tareas`)
    manage.py
    tareas/
    api/
    tasks/
    requirements.txt
  /frontend (Vue 3 + Vite)
    package.json
    src/
```

## 10. Comandos útiles (local)

* Crear virtualenv: `python -m venv venv`
* Activar: `venv\Scripts\activate` 
* Instalar requirements: `pip install -r requirements.txt`
* Migraciones: `python manage.py migrate`
* Ejecutar server: `python manage.py runserver`

## 11. Ejemplos de requests/responses

**Registro**

```
POST /api/register/
{ "username": "diego", "password": "diego123" }
```

Respuesta 201:

```
{ "id": 5, "username": "diego" }
```

**Obtener token**

```
POST /api/token/
{ "username": "usuario", "password": "secret" }
```

Respuesta 200:

```
{ "access": "<token>", "refresh": "<token>" }
```

**Crear tarea**

```
POST /api/tasks/  (Auth header required)
{ "title": "Comprar leche", "description": "Ir al supermercado", "date_completed": null }
```

Respuesta 201:

```
{ "id": 7, "title": "Comprar leche", "description": "Ir al supermercado", "user": 5, "date_completed": null }
```

## 12. Diagrama de arquitectura

* Frontend (Vue 3) → Backend (Django REST API) → PostgreSQL 

## 13. Notas finales y mejoras posibles

* Agregar tests automatizados (unit + integration).
* Implementar paginación y filtros por fecha, importancia.
* Implementar cantidad de solicitudes, logging estructurado, monitorización.

---


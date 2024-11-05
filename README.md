
# Cringle

Cringle es una red social diseñada para conectar personas y facilitar la interacción en un entorno amigable y accesible. Esta aplicación está construida utilizando Flask y sigue las mejores prácticas para el desarrollo web. Hasta el momento mi proyecto más grande.

## Tecnologías utilizadas 💻

Las tecnologías usadas fueron las siguientes:

- **Flask**: Framework web para Python.
- **Flask-WTF**: Extensión que simplifica el manejo de formularios en Flask.
- **WTForms**: Biblioteca para la creación de formularios en Python.
- **Bootstrap**: Framework de CSS para mejorar el diseño y la responsividad de la aplicación.
- **SQLite**: Base de datos utilizada para almacenar la información de los usuarios y sus publicaciones.

## Características

- Registro y autenticación de usuarios.
- Creación y edición de publicaciones.
- Comentarios en publicaciones.
- Interacción entre usuarios mediante "me gusta".
- Interfaz responsiva y amigable gracias a Bootstrap.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tuusuario/cringle.git
   cd cringle

2. Crea un entorno virtual e instálalo:

  ```bash
  python -m venv venv
  source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
  pip install -r requirements.txt 
  ```

3. Configura la base de datos:
```bash
flask db init
flask db migrate
flask db upgrade
```
4. Inicia la aplicación:
```
Flask run
```
5. Abre tu navegador y ve a `http://127.0.0.1:5000`.


## Contribuciones

Si deseas contribuir a Cringle, no dudes en hacer un fork del repositorio y enviar un pull request con tus cambios.

## Licencia

¡Puedes usar este proyecto como más te guste! 


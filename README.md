# MessageBoard

Esta aplicación es una demostración del uso del framework **Flask**,
el mecanismo de **Blueprints** de **Flask**, el módulo *flask-login*, y las librerías **Redis** y **Sirope**.

La funcionalidad principal de la aplicación es permitir a los usuarios publicar mensajes,
siempre y cuando estén registrados como usuarios de la aplicación. Los campos de la misma incluyen correo electrónico y contraseña,
de manera que un usuario no encontrado es registrado, y en caso contrario su contraseña es comparada. Si el registro o el *login*
es correcto, el mensaje se añade a la lista de los últimos mensajes generados por los diferentes usuarios.

# Enlaces
- <a target="_blank" href="https://flask.palletsprojects.com/">Flask</a>
- <a target="_blank" href="https://flask.palletsprojects.com/en/2.1.x/blueprints/">Flask Blueprints</a>
- <a target="_blank" href="https://pypi.org/project/Flask-Login/">Flask login</a>
- <a target="_blank" href="https://redis.io/">Redis</a>
- <a target="_blank" href="https://github.com/baltasarq/sirope/">Sirope</a>

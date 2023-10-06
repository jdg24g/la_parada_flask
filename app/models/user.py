from config.connect_to_mysql import connect_to_mysql

class User:
    """
    Representa una entidad de usuario con operaciones CRUD para una base de datos MySQL.

    Args:
        data (dict): Un diccionario que contiene los datos del usuario.

    Atributos:
        id (int): El identificador único del usuario.
        first_name (str): El nombre del usuario.
        last_name (str): El apellido del usuario.
        email (str): La dirección de correo electrónico del usuario.
        password (str): La contraseña del usuario.
        created_at (str): La marca de tiempo cuando se creó el usuario.
        updated_at (str): La marca de tiempo cuando se actualizó por última vez el usuario.
    """

    def __init__(self, data: dict) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data: dict):
        """
        Crea un nuevo usuario en la base de datos.

        Args:
            data (dict): Un diccionario que contiene los datos del usuario (nombre, apellido, correo electrónico, contraseña).

        Returns:
            dict: Un diccionario que contiene el resultado de la operación en la base de datos.
        """
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        results = connect_to_mysql(query, data)
        return results

    @classmethod
    def update(cls, data: dict):
        """
        Actualiza un usuario existente en la base de datos.

        Args:
            data (dict): Un diccionario que contiene los datos del usuario, incluido 'id' (identificador del usuario).

        Returns:
            dict: Un diccionario que contiene el resultado de la operación en la base de datos.
        """
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, password = %(password)s WHERE id = %(id)s;"
        results = connect_to_mysql(query, data)
        return results

    @classmethod
    def delete(cls, data: dict):
        """
        Elimina un usuario de la base de datos según su ID.

        Args:
            data (dict): Un diccionario que contiene el 'id' (identificador del usuario).

        Returns:
            dict: Un diccionario que contiene el resultado de la operación en la base de datos.
        """
        query = "DELETE FROM users WHERE id = %(id)s;"
        results = connect_to_mysql(query, data)
        return results

    @classmethod
    def get_by_email(cls, data: dict):
        """
        Recupera un usuario de la base de datos por su dirección de correo electrónico.

        Args:
            data (dict): Un diccionario que contiene el 'email' (dirección de correo electrónico).

        Returns:
            User or None: Una instancia de User si se encuentra el usuario, de lo contrario, None.
        """
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connect_to_mysql(query, data)
        if results:
            return cls(results[0])
        return None

    @classmethod
    def get_all(cls):
        """
        Recupera todos los usuarios de la base de datos.

        Returns:
            list: Una lista de instancias de User que representan a todos los usuarios en la base de datos.
        """
        query = "SELECT * FROM users;"
        results = connect_to_mysql(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
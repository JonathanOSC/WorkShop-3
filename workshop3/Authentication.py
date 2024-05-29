"""
This file contains the login and register for users.

Author: Jonathan Ochoa
"""

from users import User
from typing import List

class Authentication:

    def __init__(self) -> None:
        self.UsersList: List[User] = []

    def register(self, username: str, password: str, user_type: str):
        
        #Verificnado si el username está en uso
        if any(user.username == username for user in self.UsersList):
            print(f"{username} -> Ya está registrado")
        else:
            new_user = User(username, password, user_type)
            self.UsersList.append(new_user)
            print(f"{username} -> Registrado correctamente")


    def login(self, username: str, password: str) -> bool:
        
        # Verificar si el usuario y la contraseña coinciden con algún usuario registrado
        for user in self.UsersList:
            if user.username == username and user.password == password:
                print(f"{username} -> Inicio de sesión exitoso")
                return True
        print("Credenciales incorrectas")
        return False

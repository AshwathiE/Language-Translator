from typing import List


class UserService:
    def __init__(self):
        self.users: List[dict] = []

    def create_user(self, name: str, email: str):
        user = {
            "name": name, 
            "email": email,
        }

        self.users.append(user)
        return user

    def get_user(self, email: str):
        for user in self.users:
            if user["email"] == email:
                return user

        return None

    def delete_user(self, email: str):
        for user in self.users:
            if user["email"] == email:
                self.users.remove(user)
                return True

        return False


def calculate_total(users):
    total = 0

    for user in users:
        total += 1

    return total


# ---------------------------------------------------------
# INTENTIONAL SYNTAX ERROR
# ---------------------------------------------------------

def broken_function(name, email:
    user = {
        "name": name,
        "email": email
    }

    return user
from typing import Optional


class User:
    def __init__(
            self,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            username: Optional[str] = None,
    ):
        if not first_name and not last_name and not username:
            raise ValueError('Необходимо указать параметры пользователя')

        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    # Опишите метод класса with_name.
    @classmethod
    def with_name(
        cls,
        first_name: str,
        last_name: str,
    ):
        return User(
            first_name=first_name,
            last_name=last_name
        )

        # Опишите метод класса with_username.
    @classmethod
    def with_username(
        cls,
        username: str,
    ):
        if cls.is_username_allowed(username):
            return User(username=username)

        raise ValueError('Некорректное имя пользователя')

        # Опишите статический метод класса is_username_allowed.
    @staticmethod
    def is_username_allowed(username: str) -> bool:
        return not username.startswith('admin')

    # Опишите метод-свойство full_name.
    @property
    def full_name(self) -> str:
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        if self.username:
            return f'@{self.username}'

        raise ValueError('У пользователя нет ни имени, ни никнейма')


stas = User.with_name('Стас', 'Басов')

# Попробуем создать пользователя с "запрещённым" именем.
# ne_stas = User.with_username('admin_nestas_anonymous')

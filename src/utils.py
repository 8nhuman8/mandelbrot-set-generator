from string import ascii_lowercase, ascii_uppercase, digits
from random import choice
from datetime import datetime


def generate_filename(size: int=18) -> str:
    chars = ascii_lowercase + ascii_uppercase + digits
    return ''.join(choice(chars) for _ in range(size))


def get_runtime(start_date: datetime) -> None:
    print(f'\nStart date: {start_date.isoformat()}')
    print(f'End date: {datetime.now().isoformat()}')
    print(f'Program took: {datetime.now() - start_date} to run')

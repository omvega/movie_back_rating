# Movie rating

It is backend API made in Django Rest Framework for rating movies with stars.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Usage

Create default settings in folder.

```bash
rating_movies/settings.py
```

```python
ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS = [
    ...
    'api',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
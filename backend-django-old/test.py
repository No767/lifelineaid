from urllib.parse import urlparse

DATABASE_URI = "postgresql://test:test@localhost:5432/test"

print(urlparse(DATABASE_URI))
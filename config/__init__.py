class application_config:
    HOST = "0.0.0.0"
    PORT = 8000
    docs_url = None
    redoc_url = None
    allow_credentials = False
    allow_methods = ["*"]
    allow_headers = ["*"]

class database_config:
    db_url = 'db.example.com'
    db_port = "5432"
    db_username = 'username'
    db_pwd = 'password'
    db_name = "test_db"

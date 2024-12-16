CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:3080",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:4040",
    "http://localhost:5173",
    "http://localhost:8000",
]
CORS_ORIGIN_WHITELIST = ['http://localhost:3000', "http://localhost:5173", "http://localhost:8000",]
LOCAL_HOST = ['*']
ALLOWED_HOSTS = LOCAL_HOST + CORS_ALLOWED_ORIGINS
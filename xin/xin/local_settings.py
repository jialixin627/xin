# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xin',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'ATOMIC_REQUESTS': True,
        },
    }
}

# send mail settings
# FROM_MAIL = 'jialixin0627@163.com'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.163.com'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = 'jialixin0627@163.com'
# EMAIL_HOST_PASSWORD = 'hj0627jh'
# EMAIL_USE_TLS = True
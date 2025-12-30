"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# 1. Set settings module first
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# 2. Initialize Django ASGI application EARLY
# This populates the AppRegistry before importing models/routing
django_asgi_app = get_asgi_application()





from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter(
    {
         "http": django_asgi_app
    }
)

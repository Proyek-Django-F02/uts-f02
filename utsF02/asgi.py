"""
ASGI config for utsF02 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django

from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'utsF02.settings')

# application = get_asgi_application()
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_chatroom.settings")
django.setup()
# application = get_default_application() 

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import realchat.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            realchat.routing.websocket_urlpatterns
        )
    ),
}) 

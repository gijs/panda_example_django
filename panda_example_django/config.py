import os
import settings

try:
    PANDA_EXAMPLE_DJANGO_MEDIA_ROOT = settings.PANDA_EXAMPLE_DJANGO_MEDIA_ROOT
except AttributeError:
    PANDA_EXAMPLE_DJANGO_MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static')

try:
    PANDA_EXAMPLE_DJANGO_PLAYER_DIR = settings.PANDA_EXAMPLE_DJANGO_PLAYER_DIR
except AttributeError:
    PANDA_EXAMPLE_DJANGO_PLAYER_DIR = None

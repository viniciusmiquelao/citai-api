from django.apps import AppConfig
from firebase_admin import initialize_app

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        print('Starting Schedules')
        # initialize_app(credential='credential', options={ 'project_id': 'citai-2a283'})
        # from .schedules import start
        # start()

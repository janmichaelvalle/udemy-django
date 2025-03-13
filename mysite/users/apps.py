from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # Import signals when the app is ready to ensure they are activated
        '''
        • The ready() method ensures signals are imported when Django starts.
        • Without this, signals won’t work because Django doesn’t load them automatically.
        '''
        import users.signals
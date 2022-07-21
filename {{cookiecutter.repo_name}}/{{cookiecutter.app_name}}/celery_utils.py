from celery import Task
from celery import current_app as current_celery_app


def make_celery(app):
    celery = current_celery_app
    celery.config_from_object(app.config, namespace="CELERY")

    if not hasattr(celery, "flask_app"):
        celery.flask_app = app
    celery.Task = AppContextTask
    return celery


class AppContextTask(Task):
    def __call__(self, *args, **kwargs):
        with self.app.flask_app.app_context():
            Task.__call__(self, *args, **kwargs)

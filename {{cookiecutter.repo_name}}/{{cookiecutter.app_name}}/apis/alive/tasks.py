from celery.utils.log import get_task_logger

from {{cookiecutter.app_name}} import ext_celery


celery_logger = get_task_logger(__name__)


@ext_celery.celery.task(bind=True)
def test_celery(self, x, y):
    import time

    for i in range(5):
        self.update_state(state="PROGRESS", meta={"done": i, "total": 5})
        time.sleep(1)

    self.update_state(state="SUCCESS", meta={"result": x / y})
    return {"status": "Success. Task Completed!!!", "result": x / y}

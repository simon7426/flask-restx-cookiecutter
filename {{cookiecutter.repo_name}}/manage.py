from flask.cli import FlaskGroup

from {{cookiecutter.app_name}} import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)

{%- if cookiecutter.use_celery == "yes" %}
@cli.command("celery_worker")
def celery_worker():
    from watchgod import run_process
    import subprocess

    def run_worker():
        subprocess.call(
            ["celery","-A","celery_app.celery","worker","--loglevel=info"]
        )
    run_process("./project",run_worker)
{%- endif %}

if __name__ == "__main__":
    cli()

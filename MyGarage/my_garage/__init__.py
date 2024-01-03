from .celery import app as celery_app

__all__ = ('celery_app',)

# 1. Install celery
# 2. Register Celery in 'INSTALLED_APPS'
# 3. Set 'BROKER URL'
# 4. Create 'celery.py'
# 5. Register Celery in project's '__init__.py'
# 6. Create '@shared_task'

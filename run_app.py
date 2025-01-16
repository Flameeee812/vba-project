import app
import logger
from database import close_conn, connection, end_task, scheduler


if __name__ == "__main__":
    try:
        app.my_app.run(port=5005)
    except Exception as e:
        logger.app_logger.exception(f"Произошла ошибка: {e}")
    finally:
        close_conn(connection=connection)
        end_task(scheduler=scheduler)

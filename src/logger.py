import logging
import os
from datetime import datetime

def setup_logging():
    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    LOG_FILE_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE)

    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

    logging.info('Logging has started')

if __name__ == "__main__":
    setup_logging()


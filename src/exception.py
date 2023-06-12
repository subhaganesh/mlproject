import sys
import logger

def get_error_message(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in the Python script: {file_name}, Line: {line_number}, Error: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))
        self.error_message = get_error_message(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message
        
if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logger.setup_logging()
        logger.logging.error(str(e))
        raise CustomException(e, sys)



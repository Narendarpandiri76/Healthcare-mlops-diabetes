import sys
import traceback


class CustomException(Exception):
    """
    Custom exception class for the project.
    Adds file name and line number to error messages.
    """

    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = CustomException.get_detailed_error(
            error_message, error_detail
        )

    @staticmethod
    def get_detailed_error(error: Exception, error_detail: sys) -> str:
        _, _, tb = error_detail.exc_info()
        file_name = tb.tb_frame.f_code.co_filename
        line_number = tb.tb_lineno

        return (
            f"Error occurred in file [{file_name}] "
            f"at line [{line_number}] "
            f"with message [{str(error)}]"
        )

    def __str__(self):
        return self.error_message



class BrowserLaunchError(Exception):
    """
    Custom exception for browser launch failures.

    Attributes:
        message (str): Human-readable error message.
        original_exception (Exception, optional): Original exception instance.
    """

    def __init__(self, message, original_exception=None):
        super().__init__(message)
        self.original_exception = original_exception


    def __str__(self):
        if self.original_exception:
            return f"{self.args[0]} (Caused by: {repr(self.original_exception)})"
        return self.args[0]



class ConfigLoadError(Exception):
    """
    Custom exception for configuration loading failures.

    Attributes:
        message (str): Human-readable error message.
        original_exception (Exception, optional): Original exception instance.
    """

    def __init__(self, message, original_exception=None):
        super().__init__(message)
        self.original_exception = original_exception

    def __str__(self):
        if self.original_exception:
            return f"{self.args[0]} (Caused by: {repr(self.original_exception)})"
        return self.args[0]





class ElementNotFoundError(Exception):
    """
    Raised when a web element cannot be found.

    Attributes:
        message (str): Human-readable error message.
        original_exception (Exception, optional): Original exception instance.
    """

    def __init__(self, message="Element Not Found", original_exception=None):
        super().__init__(message)
        self.original_exception = original_exception

    def __str__(self):
        if self.original_exception:
            return f"{self.args[0]} (Caused by: {repr(self.original_exception)})"
        return self.args[0]




class OperationTimeoutError(Exception):
    """
    Raised when a wait or operation times out.

    Attributes:
        message (str): Human-readable error message.
        original_exception (Exception, optional): Original exception instance.
    """

    def __init__(self, message="Operation Timed Out", original_exception=None):
        super().__init__(message)
        self.original_exception = original_exception

    def __str__(self):
        if self.original_exception:
            return f"{self.args[0]} (Caused by: {repr(self.original_exception)})"
        return self.args[0]

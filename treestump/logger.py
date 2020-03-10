import logging

from treestump.formatter import TreestumpFormatter


class TreestumpLogger:
    def __init__(self, app_name: str, event_log_formatter_cls=None):
        """
        Creates the TreestumpLogger instance, using a custom formatter. The default is `TreestumpFormatter`. Any argument that overrides this default must be a subclass of `TreestumpFormatter`. If it is not, `TreestumpFormatter` will be used instead.

        @param app_name: The name of the application where the logger is being used
        @type app_name: str
        @debug_mode: (Optional) Defaults to False
        @type debug_mode: bool
        @param event_log_formatter_cls: (Optional) Log formatter for the class. Defaults to `TreestumpFormatter`. Any custom formatters should inherit from `TreestumpFormatter`.
        """
        self.app_name = app_name
        if event_log_formatter_cls:
            try:
                assert issubclass(event_log_formatter_cls, TreestumpFormatter)
                self._event_log_formatter_cls = event_log_formatter_cls
            except AssertionError:
                self.event_log_formatter_cls = TreestumpFormatter
        else:
            self.event_log_formatter_cls = TreestumpFormatter

        self._logger = self._configure_logger()

    def __repr__(self):
        return f"TreestumpLogger for application '{self.app_name}'"

    def log(self, message: str, level=20, *args, **kwargs):
        """
        @param message: The human-readable message to log
        @type message: str
        @param args: Additional arguments to pass to the logger
        @type args: list
        @param kwargs: Additional keyword arguments to pass to the logger
        @type kwargs: dict
        """
        # If no level is specified, log at 20: INFO
        self._logger.log(level, message, *args, **kwargs)

    def _configure_logger(self):
        """
        Configures the Python logger. This retreives or creates a specially-named logger where the handler is an instance of `logging.StreamHandler` and the formatter is an instance of `TreestumpFormatter`

        @return: The configured Python logger
        @rtype: logging.Logger
        """
        # Create (or retrieve) a logger named by our template and app_name
        logger = logging.getLogger(f"{self.app_name}_event_logger")

        # Set log level threshold
        logger.setLevel(logging.INFO)

        # Create a new logging.StreamHandler() and set our defined formatter on the handler
        handler = logging.StreamHandler()
        handler.setFormatter(self.event_log_formatter_cls(self.app_name))
        logger.addHandler(handler)

        return logger

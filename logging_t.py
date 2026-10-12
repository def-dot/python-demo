import logging


class SafeStreamHandler(logging.StreamHandler):
    """StreamHandler that gracefully handles closed streams during shutdown.

    This handler prevents "ValueError: I/O operation on closed file" errors
    that can occur when pytest or other test frameworks close stdout/stderr
    before Python's logging cleanup runs.
    """

    def flush(self):
        """Flush the stream, ignoring errors if the stream is closed."""
        try:
            super().flush()
        except (ValueError, OSError):
            # Stream is closed or otherwise unavailable, silently ignore
            pass

    def close(self):
        """Close the handler, ignoring errors if the stream is already closed."""
        try:
            super().close()
        except (ValueError, OSError):
            # Stream is closed or otherwise unavailable, silently ignore
            pass


# Initialize logger with basic configuration
logger = logging.getLogger("lightrag")
logger.propagate = False  # prevent log message send to root logger
logger.setLevel(logging.INFO)

# Add console handler if no handlers exist
if not logger.handlers:
    console_handler = SafeStreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


logger.info("hello world")

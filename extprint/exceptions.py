class NoSuchColorException(Exception):
    """Raised when given color is not exists"""
    def __init__(self, *args, **kwargs):
        message = "No such color, to see existing colors use show_available_colors() function"
        super().__init__(message)


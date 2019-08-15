class NoSuchColorException(Exception):
    """Raised when given color is not exists"""
    def __init__(self, *args, **kwargs):
        message = "No such color, to see existing colors pass ? as color parameter\nexample: printcolored('hi', color='?')\n"
        super().__init__(message)


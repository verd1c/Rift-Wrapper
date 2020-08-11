class RegionError(Exception):
    def __str__(self):
        return "Invalid Region Entered"


class APIKeyError(Exception):

    @property
    def __str__(self):
        return "Invalid API Key"


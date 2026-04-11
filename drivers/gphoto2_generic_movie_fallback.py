from .driver_api import GPhoto2CameraDriver


class GenericGPhoto2MovieFallbackDriver(GPhoto2CameraDriver):
    DRIVER_ID = "gphoto2_generic_movie_fallback"
    DISPLAY_NAME = "Generic gphoto2 movie fallback"
    BACKEND = "gphoto2"
    PRIORITY = 10
    IS_FALLBACK = True
    MATCH_PATTERNS = ()

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    PREVIEW_MODE = "movie"
    PREVIEW_VIEWFINDER_VALUE = "viewfinder=1"

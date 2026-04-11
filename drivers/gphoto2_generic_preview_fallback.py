from .driver_api import GPhoto2CameraDriver


class GenericGPhoto2PreviewFallbackDriver(GPhoto2CameraDriver):
    DRIVER_ID = "gphoto2_generic_preview_fallback"
    DISPLAY_NAME = "Generic gphoto2 preview fallback"
    BACKEND = "gphoto2"
    PRIORITY = 5
    IS_FALLBACK = True
    MATCH_PATTERNS = ()

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    PREVIEW_MODE = "preview"

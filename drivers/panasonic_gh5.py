from .driver_api import GPhoto2CameraDriver


class PanasonicGH5(GPhoto2CameraDriver):
    DRIVER_ID = "panasonic_gh5"
    DISPLAY_NAME = "Panasonic GH5"
    BACKEND = "gphoto2"
    PRIORITY = 95
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"panasonic.*gh5|gh5.*panasonic",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    PREVIEW_MODE = "movie"

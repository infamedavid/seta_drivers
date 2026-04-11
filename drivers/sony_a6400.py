from .driver_api import GPhoto2CameraDriver


class SonyA6400(GPhoto2CameraDriver):
    DRIVER_ID = "sony_a6400"
    DISPLAY_NAME = "Sony A6400"
    BACKEND = "gphoto2"
    PRIORITY = 100
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"sony.*a6400|a6400.*sony",)

    SETTING_KEY_TO_PATH = {
        "iso": "/main/imgsettings/iso",
        "shutter_speed": "/main/capturesettings/shutterspeed",
        "aperture": "/main/capturesettings/aperture",
    }
    SUPPORTED_SETTINGS = ["iso", "shutter_speed", "aperture"]

    PREVIEW_MODE = "movie"

from .driver_api import GPhoto2CameraDriver


class CanonEOS2000D(GPhoto2CameraDriver):
    DRIVER_ID = "canon_eos_2000d"
    DISPLAY_NAME = "Canon EOS 2000D"
    BACKEND = "gphoto2"
    PRIORITY = 100
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"canon.*eos.*2000d|eos.*2000d.*canon",)

    SETTING_KEY_TO_PATH = {
        "iso": "/main/imgsettings/iso",
        "shutter_speed": "/main/capturesettings/shutterspeed",
        "aperture": "/main/capturesettings/aperture",
    }
    SUPPORTED_SETTINGS = ["iso", "shutter_speed", "aperture"]

    PREVIEW_MODE = "movie"
    PREVIEW_VIEWFINDER_VALUE = "viewfinder=1"

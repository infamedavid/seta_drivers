from .driver_api import GPhoto2CameraDriver


class FujifilmXT3(GPhoto2CameraDriver):
    DRIVER_ID = "fujifilm_xt3"
    DISPLAY_NAME = "Fujifilm X-T3"
    BACKEND = "gphoto2"
    PRIORITY = 95
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"fujifilm.*x.*t3|x.*t3.*fujifilm",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    PREVIEW_MODE = "preview"

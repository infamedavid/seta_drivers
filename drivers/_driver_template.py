# Files starting with '_' should be ignored by discovery.

from .driver_api import GPhoto2CameraDriver


class MyCameraDriver(GPhoto2CameraDriver):
    DRIVER_ID = "my_camera_driver"
    DISPLAY_NAME = "My Camera"
    BACKEND = "gphoto2"
    PRIORITY = 50
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"my.*camera|camera.*my",)

    SETTING_KEY_TO_PATH = {
        "iso": "/main/imgsettings/iso",
    }
    SUPPORTED_SETTINGS = ["iso"]

    PREVIEW_MODE = "movie"
    PREVIEW_VIEWFINDER_VALUE = "viewfinder=1"

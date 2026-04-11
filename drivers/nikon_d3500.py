from .driver_api import GPhoto2CameraDriver


class NikonD3500(GPhoto2CameraDriver):
    DRIVER_ID = "nikon_d3500"
    DISPLAY_NAME = "Nikon D3500"
    BACKEND = "gphoto2"
    PRIORITY = 95
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"nikon.*d3500|d3500.*nikon",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    PREVIEW_MODE = "preview"

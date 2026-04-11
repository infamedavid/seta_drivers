import subprocess
from ..base_driver import BaseCameraDriver


class TemplateCamera(BaseCameraDriver):

    SETTING_KEY_TO_PATH = {
        # "iso": "/main/imgsettings/iso",
        # "shutter_speed": "/main/capturesettings/shutterspeed",
        # "aperture": "/main/capturesettings/aperture",
    }

    def __init__(self, port=None):
        self.port = port

    def _port_args(self):
        return ["--port", self.port] if self.port else []

    def connect(self):
        try:
            result = subprocess.run(
                ["gphoto2", *self._port_args(), "--summary"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            return result.returncode == 0
        except Exception:
            return False

    def capture(self, output_path):
        try:
            result = subprocess.run(
                [
                    "gphoto2",
                    *self._port_args(),
                    "--capture-image-and-download",
                    "--filename",
                    output_path,
                    "--force-overwrite",
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            return result.returncode == 0
        except Exception:
            return False

    def build_preview_source_cmd(self):
        return [
            "gphoto2",
            *self._port_args(),
            "--capture-preview",
            "--stdout",
        ]

    def get_preview_cleanup_patterns(self):
        return [r"gphoto2 .*--stdout"]

    def get_capabilities(self):
        return {
            "backend": "gphoto2",
            "driver_id": "template_camera",
            "supports_capture": True,
            "supports_preview": True,
            "settings": list(self.SETTING_KEY_TO_PATH.keys()),
            "supported_settings": list(self.SETTING_KEY_TO_PATH.keys()),
        }
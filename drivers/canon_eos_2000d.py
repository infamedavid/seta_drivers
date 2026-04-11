import subprocess
from ..base_driver import BaseCameraDriver


class CanonEOS2000D(BaseCameraDriver):

    SETTING_KEY_TO_PATH = {
        "iso": "/main/imgsettings/iso",
        "shutter_speed": "/main/capturesettings/shutterspeed",
        "aperture": "/main/capturesettings/aperture",
    }

    def __init__(self, port=None):
        self.port = port

    def _port_args(self):
        return ["--port", self.port] if self.port else []

    def _resolve_config_path(self, key: str):
        return self.SETTING_KEY_TO_PATH.get(key)

    # Connection
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

    # Capture
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

    # Preview
    def build_preview_source_cmd(self):
        return [
            "gphoto2",
            *self._port_args(),
            "--set-config",
            "viewfinder=1",
            "--capture-movie",
            "--stdout",
        ]

    def get_preview_cleanup_patterns(self):
        return [r"gphoto2 .*--capture-movie .*--stdout"]

    # Settings (idéntico patrón al driver base Canon)
    def get_setting(self, key):
        config_path = self._resolve_config_path(key)
        if not config_path:
            return None
        try:
            result = subprocess.run(
                ["gphoto2", *self._port_args(), "--get-config", config_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if result.returncode != 0:
                return None
            return self._parse_config_output(result.stdout)
        except Exception:
            return None

    def _parse_config_output(self, text):
        lines = text.splitlines()
        current = None
        choices = []
        for line in lines:
            line = line.strip()
            if line.startswith("Current:"):
                current = line.replace("Current:", "").strip()
            if line.startswith("Choice:"):
                parts = line.split(" ", 2)
                if len(parts) >= 3:
                    choices.append(parts[2].strip())
        return {"current": current, "choices": choices}

    def set_setting(self, key, value):
        config_path = self._resolve_config_path(key)
        if not config_path:
            return False
        try:
            result = subprocess.run(
                [
                    "gphoto2",
                    *self._port_args(),
                    "--set-config",
                    f"{config_path}={value}",
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            return result.returncode == 0
        except Exception:
            return False

    def get_capabilities(self):
        return {
            "backend": "gphoto2",
            "driver_id": "canon_eos_2000d",
            "supports_capture": True,
            "supports_preview": True,
            "settings": list(self.SETTING_KEY_TO_PATH.keys()),
            "supported_settings": list(self.SETTING_KEY_TO_PATH.keys()),
        }
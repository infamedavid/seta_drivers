import subprocess

from ..base_driver import BaseCameraDriver


class GPhoto2CandidateDriver(BaseCameraDriver):
    """
    Conservative gphoto2 candidate driver base.

    This base exists to support driver-selection testing and exploratory camera
    trials without claiming per-model support beyond the evidence already
    documented in the research.

    Rules encoded here:
    - connection uses gphoto2 --summary
    - capture uses gphoto2 --capture-image-and-download --filename ... --force-overwrite
    - preview uses a generic gphoto2 stdout preview flow when the subclass enables it
    - no camera settings are exposed unless explicit per-model config paths are documented
    """

    DISPLAY_NAME = "Unknown Camera"
    DRIVER_ID = "unknown_gphoto2_candidate"
    SETTING_KEY_TO_PATH = {}
    PREVIEW_SOURCE_ARGS = ["--capture-movie", "--stdout"]
    PREVIEW_CLEANUP_PATTERN = r"gphoto2 .*--capture-movie .*--stdout"
    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Experimental candidate driver generated from the research pack."

    def __init__(self, port=None):
        self.port = port

    def _port_args(self):
        if self.port:
            return ["--port", self.port]
        return []

    def _resolve_config_path(self, key: str):
        return self.SETTING_KEY_TO_PATH.get(key)

    def connect(self):
        try:
            result = subprocess.run(
                ["gphoto2", *self._port_args(), "--summary"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            if result.returncode == 0:
                print(f"{self.DISPLAY_NAME} connected ({self.port or 'auto-detect'})")
                return True

            print(f"{self.DISPLAY_NAME} connection error:", result.stderr)
            return False
        except Exception as e:
            print(f"{self.DISPLAY_NAME} connection exception:", e)
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

            if result.returncode == 0:
                print("Image captured:", output_path)
                return True

            print(f"{self.DISPLAY_NAME} capture error:", result.stderr)
            return False
        except Exception as e:
            print(f"{self.DISPLAY_NAME} capture exception:", e)
            return False

    def build_preview_source_cmd(self):
        if not self.PREVIEW_SOURCE_ARGS:
            return None

        return [
            "gphoto2",
            *self._port_args(),
            *self.PREVIEW_SOURCE_ARGS,
        ]

    def get_preview_cleanup_patterns(self):
        if not self.PREVIEW_CLEANUP_PATTERN:
            return []
        return [self.PREVIEW_CLEANUP_PATTERN]

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
                print(f"{self.DISPLAY_NAME} get setting error:", result.stderr)
                return None

            return self._parse_config_output(result.stdout)
        except Exception as e:
            print(f"{self.DISPLAY_NAME} get setting exception:", e)
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

        return {
            "current": current,
            "choices": choices,
        }

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

            if result.returncode == 0:
                print(f"Set {key} -> {value}")
                return True

            print(f"{self.DISPLAY_NAME} set setting error:", result.stderr)
            return False
        except Exception as e:
            print(f"{self.DISPLAY_NAME} set setting exception:", e)
            return False

    def get_capabilities(self):
        settings = list(self.SETTING_KEY_TO_PATH.keys())
        return {
            "backend": "gphoto2",
            "driver_id": self.DRIVER_ID,
            "supports_capture": True,
            "supports_preview": bool(self.PREVIEW_SOURCE_ARGS),
            "settings": settings,
            "supported_settings": settings,
            "evidence_status": self.EVIDENCE_STATUS,
            "support_tier": self.SUPPORT_TIER,
            "candidate_driver": True,
            "evidence_summary": self.EVIDENCE_SUMMARY,
        }

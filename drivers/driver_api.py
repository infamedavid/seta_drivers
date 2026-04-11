import re
import subprocess
from typing import Any


class CameraDriver:
    """Repositorio-local driver contract base."""

    DRIVER_ID = ""
    DISPLAY_NAME = ""
    BACKEND = ""
    PRIORITY = 0
    IS_FALLBACK = False
    MATCH_PATTERNS: tuple[str, ...] = ()
    SETTING_KEY_TO_PATH: dict[str, str] = {}
    SUPPORTED_SETTINGS: list[str] = []
    ABSTRACT = False

    def __init__(self, port: str | None = None):
        self.port = port

    @classmethod
    def matches_device(cls, camera_name: str | None = None, **_: Any) -> bool:
        if not camera_name:
            return False
        lowered = camera_name.lower()
        return any(re.search(pattern, lowered) for pattern in cls.MATCH_PATTERNS)


class GPhoto2CameraDriver(CameraDriver):
    """Base compartida y reusable para drivers gphoto2."""

    BACKEND = "gphoto2"
    ABSTRACT = False
    PREVIEW_MODE = "movie"  # movie | preview | none
    PREVIEW_VIEWFINDER_VALUE: str | None = None
    PREVIEW_CLEANUP_REGEX: str | None = None

    def _port_args(self) -> list[str]:
        return ["--port", self.port] if self.port else []

    def _resolve_config_path(self, key: str) -> str | None:
        return self.SETTING_KEY_TO_PATH.get(key)

    def connect(self) -> bool:
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

    def capture(self, output_path: str) -> bool:
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

    def build_preview_source_cmd(self) -> list[str] | None:
        if self.PREVIEW_MODE == "none":
            return None

        cmd = ["gphoto2", *self._port_args()]
        if self.PREVIEW_VIEWFINDER_VALUE:
            cmd.extend(["--set-config", self.PREVIEW_VIEWFINDER_VALUE])

        if self.PREVIEW_MODE == "preview":
            cmd.extend(["--capture-preview", "--stdout"])
        else:
            cmd.extend(["--capture-movie", "--stdout"])

        return cmd

    def get_preview_cleanup_patterns(self) -> list[str]:
        if self.PREVIEW_CLEANUP_REGEX:
            return [self.PREVIEW_CLEANUP_REGEX]

        if self.PREVIEW_MODE == "preview":
            return [r"gphoto2 .*--capture-preview .*--stdout"]
        if self.PREVIEW_MODE == "movie":
            return [r"gphoto2 .*--capture-movie .*--stdout"]
        return []

    def _parse_config_output(self, text: str) -> dict[str, Any]:
        lines = text.splitlines()
        current = None
        choices = []

        for line in lines:
            stripped = line.strip()
            if stripped.startswith("Current:"):
                current = stripped.replace("Current:", "").strip()
            if stripped.startswith("Choice:"):
                parts = stripped.split(" ", 2)
                if len(parts) >= 3:
                    choices.append(parts[2].strip())

        return {"current": current, "choices": choices}

    def get_setting(self, key: str) -> dict[str, Any] | None:
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

    def set_setting(self, key: str, value: str) -> bool:
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

    def get_capabilities(self) -> dict[str, Any]:
        return {
            "backend": self.BACKEND,
            "driver_id": self.DRIVER_ID,
            "supports_capture": True,
            "supports_preview": self.PREVIEW_MODE != "none",
            "settings": self.SUPPORTED_SETTINGS,
            "supported_settings": self.SUPPORTED_SETTINGS,
            "is_fallback": bool(self.IS_FALLBACK),
            "priority": int(self.PRIORITY),
        }


def validate_driver_class(driver_cls: type[CameraDriver]) -> list[str]:
    errors = []
    if not getattr(driver_cls, "DRIVER_ID", ""):
        errors.append("DRIVER_ID vacío")
    if not getattr(driver_cls, "DISPLAY_NAME", ""):
        errors.append("DISPLAY_NAME vacío")
    if not getattr(driver_cls, "BACKEND", ""):
        errors.append("BACKEND vacío")
    try:
        int(getattr(driver_cls, "PRIORITY"))
    except Exception:
        errors.append("PRIORITY no interpretable como int")
    if not isinstance(getattr(driver_cls, "IS_FALLBACK", None), bool):
        errors.append("IS_FALLBACK no interpretable como bool")

    if not driver_cls.IS_FALLBACK:
        has_patterns = bool(getattr(driver_cls, "MATCH_PATTERNS", ()))
        custom_match = driver_cls.matches_device is not CameraDriver.matches_device
        if not (has_patterns or custom_match):
            errors.append("driver específico sin MATCH_PATTERNS ni matches_device custom")

    return errors

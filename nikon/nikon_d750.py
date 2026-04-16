from seta.gphoto2_driver import GPhoto2CameraDriver


class NikonD750Experimental(GPhoto2CameraDriver):
    DRIVER_ID = 'nikon_d750_experimental'
    DISPLAY_NAME = 'Nikon D750 (Experimental)'
    BACKEND = "gphoto2"
    PRIORITY = 80
    IS_FALLBACK = False
    MATCH_PATTERNS = (
        'nikon.*\\bd750\\b',
        'nikon d750',
        '\\bd750\\b.*nikon',
    )

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    RESEARCH_VERDICT = 'pass'
    SUPPORT_LEVEL = "laboratory"
    PREVIEW_STRATEGY = 'plain_movie'
    RESEARCH_NOTES = 'Report shortlist PASS candidate; preview path still treated as laboratory flow in SETA.'
    PREVIEW_CLEANUP_REGEX = 'gphoto2 .*--capture-movie .*--stdout'


    def build_preview_source_cmd(self):
        return [
            "gphoto2",
            *self._port_args(),
            "--capture-movie",
            "--stdout",
        ]


    def get_capabilities(self):
        caps = dict(super().get_capabilities() or {})
        caps.update(
            {
                "experimental": True,
                "support_level": self.SUPPORT_LEVEL,
                "research_verdict": self.RESEARCH_VERDICT,
                "preview_strategy": self.PREVIEW_STRATEGY,
                "research_notes": self.RESEARCH_NOTES,
            }
        )
        return caps

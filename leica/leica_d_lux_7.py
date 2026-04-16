from seta.gphoto2_driver import GPhoto2CameraDriver


class LeicaDLux7Experimental(GPhoto2CameraDriver):
    DRIVER_ID = 'leica_d_lux_7_experimental'
    DISPLAY_NAME = 'Leica D-Lux 7 (Experimental)'
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (
        'leica.*d[-_ ]?lux\\s*7',
        'd[-_ ]?lux\\s*7.*leica',
        '\\bdlux\\s*7\\b',
    )

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    RESEARCH_VERDICT = 'uncertain'
    SUPPORT_LEVEL = "laboratory"
    PREVIEW_STRATEGY = 'plain_movie'
    RESEARCH_NOTES = 'Market demand is noted in research, but gphoto2 workflow is not proven there.'
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

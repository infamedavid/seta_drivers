from seta.gphoto2_driver import GPhoto2CameraDriver


class SonyAlphaA7IIIExperimental(GPhoto2CameraDriver):
    DRIVER_ID = 'sony_alpha_a7_iii_experimental'
    DISPLAY_NAME = 'Sony Alpha A7 III (Experimental)'
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (
        'sony.*a7\\s*iii',
        'sony.*a7\\s*3',
        'alpha a7\\s*(iii|3)',
        'a7\\s*(iii|3).*sony',
    )

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    RESEARCH_VERDICT = 'uncertain'
    SUPPORT_LEVEL = "laboratory"
    PREVIEW_STRATEGY = 'plain_movie'
    RESEARCH_NOTES = 'Model is commercially strong in research, but gphoto2 workflow remains unproven there.'
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

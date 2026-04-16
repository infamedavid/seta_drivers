from seta.gphoto2_driver import GPhoto2CameraDriver


class FujifilmXT3Experimental(GPhoto2CameraDriver):
    DRIVER_ID = 'fujifilm_xt3_experimental'
    DISPLAY_NAME = 'Fujifilm X-T3 (Experimental)'
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (
        'fujifilm.*x\\s*[-_ ]?t3',
        'fuji.*x\\s*[-_ ]?t3',
        '\\bx-t3\\b',
        '\\bxt3\\b',
    )

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    RESEARCH_VERDICT = 'uncertain'
    SUPPORT_LEVEL = "laboratory"
    PREVIEW_STRATEGY = 'plain_movie'
    RESEARCH_NOTES = 'Commercial relevance is documented in research; command flow remains experimental.'
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

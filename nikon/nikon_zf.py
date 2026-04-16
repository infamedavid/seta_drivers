from seta.gphoto2_driver import GPhoto2CameraDriver


class NikonZfExperimental(GPhoto2CameraDriver):
    DRIVER_ID = 'nikon_zf_experimental'
    DISPLAY_NAME = 'Nikon Zf (Experimental)'
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (
        'nikon.*\\bzf\\b',
        'nikon zf',
        '\\bzf\\b.*nikon',
    )

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    RESEARCH_VERDICT = 'uncertain'
    SUPPORT_LEVEL = "laboratory"
    PREVIEW_STRATEGY = 'plain_movie'
    RESEARCH_NOTES = 'Commercially relevant in research, but core command flow is not proven there.'
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

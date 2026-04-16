from seta.gphoto2_driver import GPhoto2CameraDriver


class OlympusOMDEM10MarkIVExperimental(GPhoto2CameraDriver):
    DRIVER_ID = 'olympus_omd_em10_mark_iv_experimental'
    DISPLAY_NAME = 'Olympus OM-D E-M10 Mark IV (Experimental)'
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (
        'olympus.*e[-_ ]?m10.*mark.*(iv|4)',
        'om[-_ ]?d.*e[-_ ]?m10.*mark.*(iv|4)',
        'e[-_ ]?m10.*mark.*(iv|4)',
    )

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    RESEARCH_VERDICT = 'uncertain'
    SUPPORT_LEVEL = "laboratory"
    PREVIEW_STRATEGY = 'plain_movie'
    RESEARCH_NOTES = 'Research does not document a closed command flow; this remains laboratory only.'
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

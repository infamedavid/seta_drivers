from seta.gphoto2_driver import GPhoto2CameraDriver


class PhaseOneXFIQ4Experimental(GPhoto2CameraDriver):
    DRIVER_ID = 'phase_one_xf_iq4_experimental'
    DISPLAY_NAME = 'Phase One XF IQ4 (Experimental)'
    BACKEND = "gphoto2"
    PRIORITY = 50
    IS_FALLBACK = False
    MATCH_PATTERNS = (
        'phase one.*xf.*iq4',
        'xf.*iq4.*phase one',
        '\\biq4\\b',
    )

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    RESEARCH_VERDICT = 'uncertain'
    SUPPORT_LEVEL = "laboratory"
    PREVIEW_STRATEGY = 'plain_movie'
    RESEARCH_NOTES = 'Research treats this as niche and not fully documented for gphoto2; laboratory only.'
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

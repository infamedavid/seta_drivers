from seta.gphoto2_driver import GPhoto2CameraDriver


class CanonEOSR6Experimental(GPhoto2CameraDriver):
    DRIVER_ID = 'canon_eos_r6_experimental'
    DISPLAY_NAME = 'Canon EOS R6 (Experimental)'
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (
        'canon.*eos.*r6',
        'eos r6.*canon',
        '\\br6\\b.*canon',
        'canon.*\\br6\\b',
    )

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    RESEARCH_VERDICT = 'uncertain'
    SUPPORT_LEVEL = "laboratory"
    PREVIEW_STRATEGY = 'canon_viewfinder_movie'
    RESEARCH_NOTES = 'ID-level evidence exists in research; this driver is a lab extrapolation, not validated support.'
    PREVIEW_CLEANUP_REGEX = 'gphoto2 .*--set-config viewfinder=1 .*--capture-movie .*--stdout'
    PREVIEW_VIEWFINDER_VALUE = 'viewfinder=1'


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

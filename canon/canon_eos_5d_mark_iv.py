from seta.gphoto2_driver import GPhoto2CameraDriver


class CanonEOS5DMarkIVExperimental(GPhoto2CameraDriver):
    DRIVER_ID = 'canon_eos_5d_mark_iv_experimental'
    DISPLAY_NAME = 'Canon EOS 5D Mark IV (Experimental)'
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (
        'canon.*eos.*5d.*mark.*(iv|4)',
        'canon.*5d.*mark.*(iv|4)',
        'eos 5d mark (iv|4)',
        '5d mark (iv|4).*canon',
    )

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    RESEARCH_VERDICT = 'uncertain'
    SUPPORT_LEVEL = "laboratory"
    PREVIEW_STRATEGY = 'canon_viewfinder_movie'
    RESEARCH_NOTES = 'Model appears in research as commercially relevant but not fully documented for all core functions.'
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

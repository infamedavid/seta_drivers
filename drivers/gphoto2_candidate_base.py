from .driver_api import GPhoto2CameraDriver


class GPhoto2CandidateDriver(GPhoto2CameraDriver):
    """Base para drivers candidatos con metadata de evidencia."""

    DRIVER_ID = "unknown_gphoto2_candidate"
    DISPLAY_NAME = "Unknown Camera"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = ()
    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    PREVIEW_MODE = "movie"

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Experimental candidate driver generated from the research pack."

    def get_capabilities(self):
        capabilities = super().get_capabilities()
        capabilities.update(
            {
                "candidate_driver": True,
                "evidence_status": self.EVIDENCE_STATUS,
                "support_tier": self.SUPPORT_TIER,
                "evidence_summary": self.EVIDENCE_SUMMARY,
            }
        )
        return capabilities

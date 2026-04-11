from .gphoto2_candidate_base import GPhoto2CandidateDriver


class PhaseOneXFIQ4(GPhoto2CandidateDriver):
    DRIVER_ID = "phase_one_xf_iq4"
    DISPLAY_NAME = "Phase One XF IQ4"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"phase.*one.*xf.*iq4|one.*xf.*iq4.*phase",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report. Mainstream coverage exists, but per-model gphoto2 workflow evidence is insufficient."

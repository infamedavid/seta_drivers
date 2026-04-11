from .gphoto2_candidate_base import GPhoto2CandidateDriver


class CanonEOSR6(GPhoto2CandidateDriver):
    DRIVER_ID = "canon_eos_r6"
    DISPLAY_NAME = "Canon EOS R6"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"canon.*eos.*r6|eos.*r6.*canon",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report. USB ID / release-note evidence exists, but core workflow evidence remains insufficient."

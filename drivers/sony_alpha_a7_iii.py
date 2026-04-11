from .gphoto2_candidate_base import GPhoto2CandidateDriver


class SonyAlphaA7III(GPhoto2CandidateDriver):
    DRIVER_ID = "sony_alpha_a7_iii"
    DISPLAY_NAME = "Sony Alpha A7 III"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"sony.*alpha.*a7.*iii|alpha.*a7.*iii.*sony",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report. USB ID and general Sony live-view mentions exist, but the full per-model workflow is not documented."

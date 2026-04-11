from .gphoto2_candidate_base import GPhoto2CandidateDriver


class SonyAlphaA7IV(GPhoto2CandidateDriver):
    DRIVER_ID = "sony_alpha_a7_iv"
    DISPLAY_NAME = "Sony Alpha A7 IV"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"sony.*alpha.*a7.*iv|alpha.*a7.*iv.*sony",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report. Market relevance exists, but the full per-model gphoto2 workflow is not documented."

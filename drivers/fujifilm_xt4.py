from .gphoto2_candidate_base import GPhoto2CandidateDriver


class FujifilmXT4(GPhoto2CandidateDriver):
    DRIVER_ID = "fujifilm_xt4"
    DISPLAY_NAME = "Fujifilm X-T4"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"fujifilm.*x.*t4|x.*t4.*fujifilm",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report. Market relevance exists, but the per-model gphoto2 workflow is not documented."

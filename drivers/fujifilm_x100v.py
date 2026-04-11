from .gphoto2_candidate_base import GPhoto2CandidateDriver


class FujifilmX100V(GPhoto2CandidateDriver):
    DRIVER_ID = "fujifilm_x100v"
    DISPLAY_NAME = "Fujifilm X100V"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"fujifilm.*x100v|x100v.*fujifilm",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report. Market relevance exists, but the per-model gphoto2 workflow is not documented."

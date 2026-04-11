from .gphoto2_candidate_base import GPhoto2CandidateDriver


class NikonZf(GPhoto2CandidateDriver):
    DRIVER_ID = "nikon_zf"
    DISPLAY_NAME = "Nikon Zf"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"nikon.*zf|zf.*nikon",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report. Market relevance exists, but per-model core gphoto2 workflow evidence is insufficient."

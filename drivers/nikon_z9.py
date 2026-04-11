from .gphoto2_candidate_base import GPhoto2CandidateDriver


class NikonZ9(GPhoto2CandidateDriver):
    DRIVER_ID = "nikon_z9"
    DISPLAY_NAME = "Nikon Z9"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"nikon.*z9|z9.*nikon",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report. Market relevance exists, but per-model core gphoto2 workflow evidence is insufficient."

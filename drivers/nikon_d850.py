from .gphoto2_candidate_base import GPhoto2CandidateDriver


class NikonD850(GPhoto2CandidateDriver):
    DRIVER_ID = "nikon_d850"
    DISPLAY_NAME = "Nikon D850"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"nikon.*d850|d850.*nikon",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report with conflicting evidence: official support snippets vs reported capture failures."

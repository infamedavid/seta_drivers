from .gphoto2_candidate_base import GPhoto2CandidateDriver


class NikonD750(GPhoto2CandidateDriver):
    DRIVER_ID = "nikon_d750"
    DISPLAY_NAME = "Nikon D750"
    BACKEND = "gphoto2"
    PRIORITY = 80
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"nikon.*d750|d750.*nikon",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "pass"
    SUPPORT_TIER = "candidate_validated"
    EVIDENCE_SUMMARY = "PASS in the report. Capture + download are directly evidenced, and liveview capability is documented, with known version-sensitivity caveats."

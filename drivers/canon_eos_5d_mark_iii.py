from .gphoto2_candidate_base import GPhoto2CandidateDriver


class CanonEOS5DMarkIII(GPhoto2CandidateDriver):
    DRIVER_ID = "canon_eos_5d_mark_iii"
    DISPLAY_NAME = "Canon EOS 5D Mark III"
    BACKEND = "gphoto2"
    PRIORITY = 80
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"canon.*eos.*5d.*mark.*iii|eos.*5d.*mark.*iii.*canon",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "pass"
    SUPPORT_TIER = "candidate_validated"
    EVIDENCE_SUMMARY = "PASS in the report. Image Capture + Liveview + download ability are evidenced, but per-model settings paths remain undocumented."

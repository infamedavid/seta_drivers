from .gphoto2_candidate_base import GPhoto2CandidateDriver


class CanonEOS5DMarkIV(GPhoto2CandidateDriver):
    DRIVER_ID = "canon_eos_5d_mark_iv"
    DISPLAY_NAME = "Canon EOS 5D Mark IV"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"canon.*eos.*5d.*mark.*iv|eos.*5d.*mark.*iv.*canon",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report, but live preview, capture, and download remain insufficiently documented at model level."

from .gphoto2_candidate_base import GPhoto2CandidateDriver


class OlympusOMDEM10MarkIV(GPhoto2CandidateDriver):
    DRIVER_ID = "olympus_omd_em10_mark_iv"
    DISPLAY_NAME = "Olympus OM-D E-M10 Mark IV"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"olympus.*om.*d.*e.*m10.*mark.*iv|om.*d.*e.*m10.*mark.*iv.*olympus",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report. Commercial relevance exists, but per-model gphoto2 workflow evidence is insufficient."

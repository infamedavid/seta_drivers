from .gphoto2_candidate_base import GPhoto2CandidateDriver


class OlympusOMDEM1MarkII(GPhoto2CandidateDriver):
    DRIVER_ID = "olympus_omd_em1_mark_ii"
    DISPLAY_NAME = "Olympus OM-D E-M1 Mark II"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"olympus.*om.*d.*e.*m1.*mark.*ii|om.*d.*e.*m1.*mark.*ii.*olympus",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report. Liveview + capture are documented, but retrieval remains undocumented, so it stays experimental."

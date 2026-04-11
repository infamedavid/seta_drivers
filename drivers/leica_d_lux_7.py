from .gphoto2_candidate_base import GPhoto2CandidateDriver


class LeicaDLux7(GPhoto2CandidateDriver):
    DRIVER_ID = "leica_d_lux_7"
    DISPLAY_NAME = "Leica D-Lux 7"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"leica.*d.*lux.*7|d.*lux.*7.*leica",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report. Market relevance exists, but per-model gphoto2 workflow evidence is insufficient."

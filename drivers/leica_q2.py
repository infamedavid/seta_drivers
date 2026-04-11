from .gphoto2_candidate_base import GPhoto2CandidateDriver


class LeicaQ2(GPhoto2CandidateDriver):
    DRIVER_ID = "leica_q2"
    DISPLAY_NAME = "Leica Q2"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"leica.*q2|q2.*leica",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report. Market relevance exists, but per-model gphoto2 workflow evidence is insufficient."

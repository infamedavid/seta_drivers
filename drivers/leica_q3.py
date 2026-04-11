from .gphoto2_candidate_base import GPhoto2CandidateDriver


class LeicaQ3(GPhoto2CandidateDriver):
    DRIVER_ID = "leica_q3"
    DISPLAY_NAME = "Leica Q3"
    BACKEND = "gphoto2"
    PRIORITY = 60
    IS_FALLBACK = False
    MATCH_PATTERNS = (r"leica.*q3|q3.*leica",)

    SETTING_KEY_TO_PATH = {}
    SUPPORTED_SETTINGS = []

    EVIDENCE_STATUS = "uncertain"
    SUPPORT_TIER = "candidate_experimental"
    EVIDENCE_SUMMARY = "Candidate in the report. USB ID / release-note evidence exists, but full workflow evidence remains insufficient."

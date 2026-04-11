from .gphoto2_candidate_base import GPhoto2CandidateDriver


class LeicaQ2(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Leica Q2'
    DRIVER_ID = 'leica_q2'
    EVIDENCE_STATUS = 'uncertain'
    SUPPORT_TIER = 'candidate_experimental'
    EVIDENCE_SUMMARY = 'Candidate in the report. Market relevance exists, but per-model gphoto2 workflow evidence is insufficient.'

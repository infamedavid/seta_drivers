from .gphoto2_candidate_base import GPhoto2CandidateDriver


class LeicaQ3(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Leica Q3'
    DRIVER_ID = 'leica_q3'
    EVIDENCE_STATUS = 'uncertain'
    SUPPORT_TIER = 'candidate_experimental'
    EVIDENCE_SUMMARY = 'Candidate in the report. USB ID / release-note evidence exists, but full workflow evidence remains insufficient.'

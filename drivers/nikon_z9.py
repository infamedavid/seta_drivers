from .gphoto2_candidate_base import GPhoto2CandidateDriver


class NikonZ9(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Nikon Z9'
    DRIVER_ID = 'nikon_z9'
    EVIDENCE_STATUS = 'uncertain'
    SUPPORT_TIER = 'candidate_experimental'
    EVIDENCE_SUMMARY = 'Candidate in the report. Market relevance exists, but per-model core gphoto2 workflow evidence is insufficient.'

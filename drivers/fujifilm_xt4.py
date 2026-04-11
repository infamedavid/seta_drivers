from .gphoto2_candidate_base import GPhoto2CandidateDriver


class FujifilmXT4(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Fujifilm X-T4'
    DRIVER_ID = 'fujifilm_xt4'
    EVIDENCE_STATUS = 'uncertain'
    SUPPORT_TIER = 'candidate_experimental'
    EVIDENCE_SUMMARY = 'Candidate in the report. Market relevance exists, but the per-model gphoto2 workflow is not documented.'

from .gphoto2_candidate_base import GPhoto2CandidateDriver


class FujifilmX100V(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Fujifilm X100V'
    DRIVER_ID = 'fujifilm_x100v'
    EVIDENCE_STATUS = 'uncertain'
    SUPPORT_TIER = 'candidate_experimental'
    EVIDENCE_SUMMARY = 'Candidate in the report. Market relevance exists, but the per-model gphoto2 workflow is not documented.'

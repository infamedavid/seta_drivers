from .gphoto2_candidate_base import GPhoto2CandidateDriver


class SonyAlphaA7IV(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Sony Alpha A7 IV'
    DRIVER_ID = 'sony_alpha_a7_iv'
    EVIDENCE_STATUS = 'uncertain'
    SUPPORT_TIER = 'candidate_experimental'
    EVIDENCE_SUMMARY = 'Candidate in the report. Market relevance exists, but the full per-model gphoto2 workflow is not documented.'

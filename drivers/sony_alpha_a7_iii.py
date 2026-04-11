from .gphoto2_candidate_base import GPhoto2CandidateDriver


class SonyAlphaA7III(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Sony Alpha A7 III'
    DRIVER_ID = 'sony_alpha_a7_iii'
    EVIDENCE_STATUS = 'uncertain'
    SUPPORT_TIER = 'candidate_experimental'
    EVIDENCE_SUMMARY = 'Candidate in the report. USB ID and general Sony live-view mentions exist, but the full per-model workflow is not documented.'

from .gphoto2_candidate_base import GPhoto2CandidateDriver


class CanonEOSR6(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Canon EOS R6'
    DRIVER_ID = 'canon_eos_r6'
    EVIDENCE_STATUS = 'uncertain'
    SUPPORT_TIER = 'candidate_experimental'
    EVIDENCE_SUMMARY = 'Candidate in the report. USB ID / release-note evidence exists, but core workflow evidence remains insufficient.'

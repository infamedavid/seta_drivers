from .gphoto2_candidate_base import GPhoto2CandidateDriver


class CanonEOS5DMarkIV(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Canon EOS 5D Mark IV'
    DRIVER_ID = 'canon_eos_5d_mark_iv'
    EVIDENCE_STATUS = 'uncertain'
    SUPPORT_TIER = 'candidate_experimental'
    EVIDENCE_SUMMARY = 'Candidate in the report, but live preview, capture, and download remain insufficiently documented at model level.'

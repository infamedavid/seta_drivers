from .gphoto2_candidate_base import GPhoto2CandidateDriver


class CanonEOS5DMarkIII(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Canon EOS 5D Mark III'
    DRIVER_ID = 'canon_eos_5d_mark_iii'
    EVIDENCE_STATUS = 'pass'
    SUPPORT_TIER = 'candidate_validated'
    EVIDENCE_SUMMARY = 'PASS in the report. Image Capture + Liveview + download ability are evidenced, but per-model settings paths remain undocumented.'

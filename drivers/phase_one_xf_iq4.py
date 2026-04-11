from .gphoto2_candidate_base import GPhoto2CandidateDriver


class PhaseOneXFIQ4(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Phase One XF IQ4'
    DRIVER_ID = 'phase_one_xf_iq4'
    EVIDENCE_STATUS = 'uncertain'
    SUPPORT_TIER = 'candidate_experimental'
    EVIDENCE_SUMMARY = 'Candidate in the report. Mainstream coverage exists, but per-model gphoto2 workflow evidence is insufficient.'

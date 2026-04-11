from .gphoto2_candidate_base import GPhoto2CandidateDriver


class OlympusOMDEM10MarkIV(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Olympus OM-D E-M10 Mark IV'
    DRIVER_ID = 'olympus_omd_em10_mark_iv'
    EVIDENCE_STATUS = 'uncertain'
    SUPPORT_TIER = 'candidate_experimental'
    EVIDENCE_SUMMARY = 'Candidate in the report. Commercial relevance exists, but per-model gphoto2 workflow evidence is insufficient.'

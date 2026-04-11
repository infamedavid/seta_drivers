from .gphoto2_candidate_base import GPhoto2CandidateDriver


class OlympusOMDEM1MarkII(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Olympus OM-D E-M1 Mark II'
    DRIVER_ID = 'olympus_omd_em1_mark_ii'
    EVIDENCE_STATUS = 'uncertain'
    SUPPORT_TIER = 'candidate_experimental'
    EVIDENCE_SUMMARY = 'Candidate in the report. Liveview + capture are documented, but retrieval remains undocumented, so it stays experimental.'

from .gphoto2_candidate_base import GPhoto2CandidateDriver


class NikonD850(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Nikon D850'
    DRIVER_ID = 'nikon_d850'
    EVIDENCE_STATUS = 'uncertain'
    SUPPORT_TIER = 'candidate_experimental'
    EVIDENCE_SUMMARY = 'Candidate in the report with conflicting evidence: official support snippets vs reported capture failures.'

from .gphoto2_candidate_base import GPhoto2CandidateDriver


class NikonD750(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Nikon D750'
    DRIVER_ID = 'nikon_d750'
    EVIDENCE_STATUS = 'pass'
    SUPPORT_TIER = 'candidate_validated'
    EVIDENCE_SUMMARY = 'PASS in the report. Capture + download are directly evidenced, and liveview capability is documented, with known version-sensitivity caveats.'

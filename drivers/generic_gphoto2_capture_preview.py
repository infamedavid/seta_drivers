from .gphoto2_candidate_base import GPhoto2CandidateDriver


class GenericGPhoto2CapturePreview(GPhoto2CandidateDriver):
    DISPLAY_NAME = 'Generic gphoto2 Fallback (capture-preview)'
    DRIVER_ID = 'generic_gphoto2_capture_preview'
    PREVIEW_SOURCE_ARGS = ['--capture-preview', '--stdout']
    PREVIEW_CLEANUP_PATTERN = r'gphoto2 .*--capture-preview .*--stdout'
    EVIDENCE_STATUS = 'exploratory_generic'
    SUPPORT_TIER = 'generic_fallback'
    EVIDENCE_SUMMARY = (
        'Generic exploratory fallback for unmatched gphoto2 cameras. '
        'Uses --summary, unified capture+download, and preview via '
        '--capture-preview --stdout. This does not claim per-model support.'
    )

    def get_capabilities(self):
        capabilities = super().get_capabilities()
        capabilities.update(
            {
                'candidate_driver': False,
                'generic_fallback': True,
                'fallback_preview_mode': 'capture_preview_stdout',
            }
        )
        return capabilities

from django.core.exceptions import ValidationError
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class SizeImageFieldValidator:
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
    """

    code = "invalid_extension"

    max_upload_size: int

    def __init__(self, max_upload_size):
        self.max_upload_size = max_upload_size

    def __call__(self, value):
        file = value.file
        if file._size > self.max_upload_size:
            raise forms.ValidationError(_(
                f'Please keep filesize under {filesizeformat(self.max_upload_size)}. Current filesize {filesizeformat(file._size)}'
            ))

        return value


def validate_size_image(value):
    max_upload_size = 20971520
    file = value.file
    if file._size > max_upload_size:
        raise ValidationError(
            _('%(value)s more size'),
            params={'value': value},
        )

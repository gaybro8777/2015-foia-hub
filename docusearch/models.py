from django.db import models


class Document(models.Model):
    """ A model representing a document from an agency. """

    text = models.TextField(
        null=False, help_text='The full text of the document')
    title = models.TextField(null=True)
    date = models.DateField(null=True)
    release_agency_slug = models.CharField(
        max_length=100,
        help_text="Slug for the agency or office that released this document.")
    path = models.FilePathField(
        null=False, help_text="Path to the original document file")


    def get_absolute_url(self):
        """ Return the canonical URL for a Document object. """
        return '/documents/document/%i' % self.id
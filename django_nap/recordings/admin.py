from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from recordings.models import Recording, Transcription

# class TranscriptInline(GenericTabularInline):
    # model = Transcription
    
# class RecordingAdmin(admin.ModelAdmin):
    # inlines = [
        # TranscriptInline,
    # ]

admin.site.register(Recording)
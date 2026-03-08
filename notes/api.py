from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note


@api_view(['GET'])

def notes_api(request):

    notes = Note.objects.all().values()

    return Response(notes)
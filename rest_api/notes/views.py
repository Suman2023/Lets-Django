from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import NoteSerializer
from .models import Note
# Create your views here.


@api_view(['GET'])
def getRoutes(req):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns all the notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns notes with the given id'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {
                'body': ""
            },
            'description': 'Create a new note'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {
                'body': ""
            },
            'description': 'Update note based on passed id'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete note based on passed id'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getNotes(req):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(req, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(req):
    data = req.data
    note = Note.objects.create(
        title=data['title'],
        body=data['body'],
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(req, pk):
    data = req.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(req, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note deleted!")

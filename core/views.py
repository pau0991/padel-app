# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
from .models import CustomUser, Match
from .serializers import UserSerializer, MatchSerializer


@csrf_exempt
def users(request):
    '''
    List all user snippets
    '''
    if (request.method == 'GET'):
        # get all the users
        users = CustomUser.objects.all()
        # serialize the user data
        serializer = UserSerializer(users, many=True)
        # return a Json response
        return JsonResponse(serializer.data, safe=False)

    elif (request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = UserSerializer(data=data)

        # check if the sent information is okay
        if (serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_detail(request, pk):
    try:
        # obtain the user with the passed id.
        user = CustomUser.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)

    if (request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = UserSerializer(user, data=data)
        # check whether the sent information is okay
        if (serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

    elif (request.method == 'DELETE'):
        # delete the user
        user.delete()
        # return a no content response.
        return HttpResponse(status=204)


@csrf_exempt
def matches(request):
    '''
    List all match snippets
    '''
    if (request.method == 'GET'):
        # get all the users
        matches = Match.objects.all()
        # serialize the match data
        serializer = MatchSerializer(matches, many=True)
        # return a Json response
        return JsonResponse(serializer.data, safe=False)

    elif (request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = MatchSerializer(data=data)

        # check if the sent information is okay
        if (serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def match_detail(request, pk):
    try:
        # obtain the match with the passed id.
        match = Match.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)

    if (request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = MatchSerializer(match, data=data)
        # check whether the sent information is okay
        if (serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

    elif (request.method == 'DELETE'):
        # delete the match
        match.delete()
        # return a no content response.
        return HttpResponse(status=204)
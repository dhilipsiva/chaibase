# Django
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import logout as dj_logout, authenticate

# Django 3rd party
from tokenapi.tokens import token_generator

# ChaiBase
from chaibase.core.dbapi import get_user


@csrf_exempt
def login(request):
    username = request.POST.get('username', "").strip()
    password = request.POST.get('password', "").strip()

    if username == "" or password == "":
        return JsonResponse({
            "message": "both 'username' and 'password' needed"}, status=403)

    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({
            "message": "Unable to log you in, please try again."}, status=403)

    if not user.is_active:
        return JsonResponse({
            "message": "User account is disabled."}, status=403)
    data = {
        'token': token_generator.make_token(user),
        'user_id': str(user.pk),
    }
    return JsonResponse(data)


@csrf_exempt
def check(request):
    token = request.POST.get('token', "").strip()
    user_uuid = request.POST.get('user_id', '').strip()
    user = get_user(pk=user_uuid)

    if not user:
        JsonResponse(
            {"message": "Please send a valid user_id"}, status=403)

    if token_generator.check_token(user, token) and user.is_active:
        return JsonResponse(request.POST)

    return JsonResponse({
        "message": "Unable to log you in, please try again."}, status=403)


@csrf_exempt
def logout(request):
    dj_logout(request)
    return JsonResponse(
            {'message': 'Logout out succcessfully!'}, status=200)

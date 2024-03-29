# Standard imports

# Django
from django.http import JsonResponse
from django.contrib.auth import logout as dj_logout, authenticate

# Django 3rd party
from tokenapi.decorators import token_required

# ChaiBase
from chaibase.core.dbapi import get_browser, create_browser, update_browser, \
    get_user, get_factory


def login(request):
    identification = request.POST.get('identification', "").strip()
    password = request.POST.get('password', "").strip()

    if identification == "" or password == "":
        return JsonResponse({
            "message": "both 'identification' and 'password' needed"},
            status=403)

    user = authenticate(username=identification, password=password)
    if user is None:
        user = authenticate(email=identification, password=password)

    if user is None:
        return JsonResponse({
            "message": "Invalid Credentials"}, status=403)

    if user.is_active is False:
        return JsonResponse({
            "message": "User account is disabled."}, status=403)

    return JsonResponse({"user_id": user.id, "token": user.b64token})


def check(request):
    token = request.POST.get('token', "").strip()
    user_id = request.POST.get('user_id', '').strip()
    user = get_user(user_id)
    if user is None or user.check_token(token):
        return JsonResponse({
            "message": "Invalid User / Token"}, status=403)
    return JsonResponse({"user_id": user.id, "token": user.b64token})


def logout(request):
    dj_logout(request)
    return JsonResponse(
            {'message': 'Logout out succcessfully!'}, status=200)


def browser(request, fingerprint):
    """
    Fingerprinting browsers
    """
    _browser = get_browser(fingerprint)
    if _browser is None:
        _browser = create_browser(fingerprint, request.POST)
    else:
        _browser = update_browser(_browser, request.POST)
    return JsonResponse(_browser.to_dict())


@token_required
def user(request, user_id):
    _user = get_user(user_id)
    return JsonResponse({'data': _user.to_dict(with_sensitive_data=True)})


@token_required
def factories(request, factory_id=None):
    """
    Get all factories
    """
    if factory_id is not None:
        factory = get_factory(id=factory_id)
        return JsonResponse({'data': factory.to_dict()})

    _factories = []

    for factory in request.user.all_factories():
        _factories.append(factory.to_dict())
    return JsonResponse({'data': _factories})

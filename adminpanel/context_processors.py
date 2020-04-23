from django.conf import settings


def global_settings(request):
    # return any necessary values
    return {
        'STATUS_ACTIVE': 1,
        'STATUS_BLOCK': 2
    }

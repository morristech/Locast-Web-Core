from django.conf import settings

def settings_variables(request):
    '''
    Allows settings to define which variables
    it wants to expose to templates
    '''

    d = {}

    if getattr(settings, 'CONTEXT_VARIABLES', None):
        for var in settings.CONTEXT_VARIABLES:
            if hasattr(settings, var):
                d[var] = getattr(settings, var)

    return d


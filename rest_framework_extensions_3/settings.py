# -*- coding: utf-8 -*-
from django.conf import settings

from rest_framework_3.settings import APISettings


USER_SETTINGS = getattr(settings, 'REST_FRAMEWORK_EXTENSIONS_3', None)

DEFAULTS = {
    # caching
    'DEFAULT_USE_CACHE': 'default',
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': None,
    'DEFAULT_CACHE_ERRORS': True,
    'DEFAULT_CACHE_KEY_FUNC': 'rest_framework_extensions_3.utils.default_cache_key_func',
    'DEFAULT_OBJECT_CACHE_KEY_FUNC': 'rest_framework_extensions_3.utils.default_object_cache_key_func',
    'DEFAULT_LIST_CACHE_KEY_FUNC': 'rest_framework_extensions_3.utils.default_list_cache_key_func',

    # ETAG
    'DEFAULT_ETAG_FUNC': 'rest_framework_extensions_3.utils.default_etag_func',
    'DEFAULT_OBJECT_ETAG_FUNC': 'rest_framework_extensions_3.utils.default_object_etag_func',
    'DEFAULT_LIST_ETAG_FUNC': 'rest_framework_extensions_3.utils.default_list_etag_func',

    # other
    'DEFAULT_KEY_CONSTRUCTOR_MEMOIZE_FOR_REQUEST': False,
    'DEFAULT_BULK_OPERATION_HEADER_NAME': 'X-BULK-OPERATION',
    'DEFAULT_PARENT_LOOKUP_KWARG_NAME_PREFIX': 'parent_lookup_'
}

IMPORT_STRINGS = [
    'DEFAULT_CACHE_KEY_FUNC',
    'DEFAULT_OBJECT_CACHE_KEY_FUNC',
    'DEFAULT_LIST_CACHE_KEY_FUNC',
    'DEFAULT_ETAG_FUNC',
    'DEFAULT_OBJECT_ETAG_FUNC',
    'DEFAULT_LIST_ETAG_FUNC',
]


extensions_api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
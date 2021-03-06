# -*- coding: utf-8 -*-
"""This module contains a template MindMeld app configuration"""

# The namespace of the application. Used to prevent collisions in supporting services across
# applications. If not set here, the app's enclosing directory name is used.
# APP_NAMESPACE = 'app-name'

# Dictionaries for the various NLP classifier configurations

# An example decision tree model for intent classification
INTENT_CLASSIFIER_CONFIG = {
    'model_type': 'text',
    'model_settings': {
        'classifier_type': 'dtree'
    },
    'param_selection': {
        'type': 'k-fold',
        'k': 5,
        'grid': {
            #'max_features': ['log2', 'sqrt', 0.01, 1]
            'max_features': [1.0]
        },
    },
    "features": {
        "exact": {},
        'bag-of-words': {'lengths': [1]},
        'enable-stemming': True
    }
}


# Fill in the other model configurations if necessary
# DOMAIN_CLASSIFIER_CONFIG = {}
#ENTITY_RECOGNIZER_CONFIG = {}
# ROLE_CLASSIFIER_CONFIG = {}
TEXT_PREPARATION_CONFIG = {
    "preprocessors": [],
    "tokenizer": "SpacyTokenizer",
    "normalizers": [
        'RemoveAposAtEndOfPossesiveForm',
        'RemoveAdjacentAposAndSpace',
        'RemoveBeginningSpace',
        'RemoveTrailingSpace',
        'ReplaceSpacesWithSpace',
        'ReplaceUnderscoreWithSpace',
        'SeparateAposS',
        'ReplacePunctuationAtWordStartWithSpace',
        'ReplacePunctuationAtWordEndWithSpace',
        'ReplaceSpecialCharsBetweenLettersAndDigitsWithSpace',
        'ReplaceSpecialCharsBetweenDigitsAndLettersWithSpace',
        'ReplaceSpecialCharsBetweenLettersWithSpace',
        'Lowercase',
        'ASCIIFold'
    ],
    "regex_norm_rules": [],
    "stemmer": "EnglishNLTKStemmer",
    "keep_special_chars": r"\@\[\]'"
}

# A example configuration for the parser
"""
# *** Note: these are place holder entity types ***
PARSER_CONFIG = {
    'grandparent': {
        'parent': {},
        'child': {'max_instances': 1}
    },
    'parent': {
        'child': {'max_instances': 1}
    }
}
"""

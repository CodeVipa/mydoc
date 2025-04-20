from collections import ChainMap
defaults_settings={
    'theme': 'light',
    'show_notifications': True,
    'autosave': False,
    'language': 'English'
}
user_settings= {
    'theme': 'dark',
    'show_notifications': False
}
environment_settings={
    'autosave': True,
    'language': 'French'
}
effective_settings= ChainMap(user_settings,environment_settings)
print(effective_settings)

from collections import ChainMap
#revision


defaults={'theme':'light','show_sidebar':'true'}
user_settings={'theme':'dark'}


settings=ChainMap(defaults,user_settings)
print(settings['theme'])    
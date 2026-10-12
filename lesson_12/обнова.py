import sys
import json


print('json loaded:', 'json' in sys.modules) # in 3.15 false
config = json.dumps({'there': 'dark', 'autosave': True})
print('json loaded:', 'json' in sys.modules)
print(config)
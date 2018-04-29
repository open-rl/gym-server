import os
import logging

# Load appropriate settings
environment = os.environ.get('RUNTIME_ENV', 'dev')

if environment == 'production':
    from gym_server.settings.prod import *
elif environment == 'staging':
    from gym_server.settings.staging import *
else:
    from gym_server.settings.dev import *

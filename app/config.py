"""module to store variables used for configuration of FLASK"""

import os


class Config(object):
    """Config class for writing config variables while setting up the Flask environment"""

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this_is_a_hard_pass'

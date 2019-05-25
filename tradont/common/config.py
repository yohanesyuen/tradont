from __future__ import print_function
import yaml
import os
import sys

#
# The default environment variable that points to the location of the tradont
# configuration file
#
DEFAULT_ENV = "TRADONT_CONF"

#
# The default path for the tradont configuration file
#
DEFAULT_PATH = "~/tradont.cfg"

class ConfigPathError(Exception):
    """
    Exception that indicates that the path specifed for a tradont config file
    location doesn't exist
    """

    def __init__(self, path):
        self.path = path

    def __str__(self):
        return "Config file '{}' could not be loaded.".format(self.path)


class ConfigValueError(Exception):
    """
    Exception that indicates that the tradont config file is missing
    a required value
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Config is missing value for '{}'.".format(self.value)

class Config(object):
    def __init__(self):
        """
        Initialize an empty Config object
        """
        self.db_config = dict.fromkeys([
            'hostname',
            'username',
            'password',
            'database'
        ])
    def __str__(self):
        """
        Create the string (YAML) representaion of the Config instance
        """
        properties = {}
        properties['db_config'] = self.db_config
        return yaml.dump(properties, default_flow_style=False)

    def dump(self, path):
        """
        Dump the YAML representation of the Config instance to a file.
        Args:
            path: The location to write the config YAML
        """

        path = os.path.expanduser(path)

        with open(path, "w") as f:
            print(self, file=f)

    def load_db_config(self,config_dict):
        for k, v in config_dict.items():
            if k in self.db_config:
                self.db_config[k] = v

    def load(self, path=DEFAULT_PATH):
        """
        Load the YAML config representation from a file into the Config instance

        Args:
            path: The location to read the config YAML from
        """

        self.path = path

        try:
            with open(os.path.expanduser(path)) as f:
                y = yaml.load(f, Loader=yaml.FullLoader)
                for k,v in y.items():
                    if k == 'db_config':
                        self.load_db_config(v)
        except:
            raise ConfigPathError(path)

    def validate(self):
        """
        Ensure that the Config instance is valid
        """

        for k, v in self.db_config.items():
            if k is None:
                raise ConfigValueError('db_config.{}'.format(k))
        return True

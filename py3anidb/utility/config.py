"""Load and manage module configuration."""

import configparser
import os.path
import sys

class Config:
    """Load and manage module configuration."""

    def __init__(self, configfilename = None):
        self._config = configparser.SafeConfigParser()
        if configfilename == None:
            self._configfilename = os.path.basename(os.path.splitext(sys.argv[0])[0]) + '.cfg'
        else:
            self._configfilename = configfilename
        if os.path.isfile(self._configfilename):
            self._config.read([self._configfilename])
        else:
            with open(self._configfilename, 'w') as configfile:
                self._config.write(configfile)

    def __repr__(self):
        return repr(self._config._sections)

    def config(self):
        return self._config

    def set_default(self, section, default):
        if self._config.has_section(section):
            return
        self._config._sections[section] = default
        with open(self._configfilename, 'w') as configfile:
            self._config.write(configfile)

    def get_section(self, section):
        if self._config.has_section(section):
            return self._config._sections[section]
        return None

    def get(self, section, option):
        return self._config.get(section, option)
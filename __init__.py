"""
Add a description of the plugin (to be presented to the user inside the wizard)
here.  This should describe *what* the plugin does.
"""

import supybot
import supybot.world as world

__version__ = ""
__author__ = supybot.Author('haliphax', 'haliphax', 'haliphax@nope')
__contributors__ = {}
__url__ = 'https://github.com/haliphax/supybot-greet'

import config
import plugin
reload(plugin)

if world.testing:
    import test

Class = plugin.Class
configure = config.configure

from time import time

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.ircmsgs as ircmsgs
import supybot.schedule as schedule

class Muzzle(callbacks.Plugin):
    """
    This plugin greets users with a defined message when they join the
    channel. In order to use this plugin, supybot.plugins.Muzzle.enable
    must be True, and supybot.plugins.Muzzle.message must be set to the
    message you wish to send to users when they join.
    """

    def __init__(self, irc):
        self.__parent = super(Muzzle, self)
        self.__parent.__init__(irc)

    def doJoin(self, irc, msg):
        channel = msg.args[0]

        if not self.registryValue('enable', channel):
            return

        delay = self.registryValue('delay', channel)

        if not ircutils.strEqual(msg.nick, irc.nick):
            irc = callbacks.SimpleProxy(irc, msg)

            def voice():
                irc.queueMsg(ircmsgs.voice(channel, msg.nick))

            schedule.addEvent(voice, time() + delay)

Class = Muzzle

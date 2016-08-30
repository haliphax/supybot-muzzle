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
    This plugin adds +v user mode to people after a delay when they join the
    channel. In order to use this plugin, supybot.plugins.Muzzle.enable
    must be True. supybot.plugins.Muzzle.delay may be set to the number of
    seconds to wait before granting +v (default 30).
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
                if msg.nick not in irc.state.channels[channel].users:
                    self.log.warn('%s is no longer in %s, cannot voice'
                                  % (msg.nick, channel))
                    return

                self.log.info('Removing muzzle from %s in %s'
                              % (msg.nick, channel))
                irc.queueMsg(ircmsgs.voice(channel, msg.nick))

            schedule.addEvent(voice, time() + delay)

Class = Muzzle

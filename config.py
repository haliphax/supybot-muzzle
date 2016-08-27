import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    conf.registerPlugin('Muzzle', True)


Muzzle = conf.registerPlugin('Muzzle')
conf.registerChannelValue(Muzzle, 'enable',
    registry.Boolean(False, """Determines whether or not the bot will
    automatically voice (after {supybot.plugins.Muzzle.delay}) users who join
    the channel."""))
conf.registerChannelValue(Muzzle, 'delay',
    registry.PositiveInteger(30, """The delay (in seconds) before a user will be
    automatically voiced after joining the channel."""))

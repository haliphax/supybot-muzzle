# supybot Muzzle plugin

This plugin will automatically grant +v to users after a specified delay when
they join the channel. Useful for preventing drive-by spam.

## settings

- `supybot.plugins.Muzzle.enable` (Boolean): Whether or not the plugin is
  active on the selected channel
- `supybot.plugins.Muzzle.delay` (PositiveInteger):  The delay (in seconds)
  before granting +v to the user

To set these, use the `config channel` command.

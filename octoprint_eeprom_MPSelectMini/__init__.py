# coding=utf-8
from __future__ import absolute_import


import octoprint.plugin
import octoprint.server

class Eeprom_MPSelectMiniPlugin(octoprint.plugin.AssetPlugin,
                            octoprint.plugin.TemplatePlugin):
    def get_assets(self):
        return dict(
            js=["js/eeprom_malyan.js"]
        )

    def get_template_configs(self):
        return [
            dict(type="settings", template="eeprom_MPSelectMini_settings.jinja2", custom_bindings=True)
        ]

    def get_update_information(self):
        return dict(
            systemcommandeditor=dict(
                displayName="EEPROM MP Select Mini Editor Plugin",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="bruhmann",
                repo="OctoPrint-EEPROM-MPSelectMini",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/bruhmann/OctoPrint-EEPROM-Marlin-MPSelectMini/archive/{target_version}.zip"
            )
        )

__plugin_name__ = "EEPROM Editor for MPSM"
__plugin_pythoncompat__ = ">=2.7,<4"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = Eeprom_MPSelectMiniPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }

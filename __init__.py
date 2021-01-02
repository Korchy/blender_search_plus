# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_search_plus

from . import search_plus_ops
from . import search_plus_ui
from . import search_plus_vars
from .addon import Addon


bl_info = {
    'name': 'search_plus',
    'category': 'All',
    'author': 'Nikita Akimov, Alexander Reshetnyak',
    'version': (1, 0, 0),
    'blender': (2, 91, 0),
    'location': 'Properties window - Render Properties tab',
    'wiki_url': 'https://b3d.interplanety.org/en/blender-add-on-youtube-search/',
    'tracker_url': 'https://b3d.interplanety.org/en/blender-add-on-youtube-search/s',
    'description': 'Quick search on youtube'
}


def register():
    if not Addon.dev_mode():
        search_plus_vars.register()
        search_plus_ops.register()
        search_plus_ui.register()
    else:
        print('It seems you are trying to use the dev version of the ' + bl_info['name'] + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        search_plus_ui.unregister()
        search_plus_ops.unregister()
        search_plus_vars.unregister()


if __name__ == '__main__':
    register()

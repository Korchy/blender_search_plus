# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_youtube_search

from . import youtube_search_ops
from . import youtube_search_ui
from . import youtube_search_vars
from .addon import Addon


bl_info = {
    'name': 'youtube_search',
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
        youtube_search_vars.register()
        youtube_search_ops.register()
        youtube_search_ui.register()
    else:
        print('It seems you are trying to use the dev version of the ' + bl_info['name'] + ' add-on. It may work not properly. Please download and use the release version')


def unregister():
    if not Addon.dev_mode():
        youtube_search_ui.unregister()
        youtube_search_ops.unregister()
        youtube_search_vars.unregister()


if __name__ == '__main__':
    register()

# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_search_plus

import bpy
from bpy.types import Operator
from bpy.props import StringProperty, BoolProperty
from bpy.utils import register_class, unregister_class


class YOUTUBE_SEARCH_OT_search(Operator):
    bl_idname = 'youtube_search.search'
    bl_label = 'Search'
    bl_description = 'Search on Youtube'
    bl_options = {'UNDO'}

    search: StringProperty(
        default=''
    )

    prefix: StringProperty(
        default=''
    )

    sort_by_date: BoolProperty(
        default=False
    )

    region: StringProperty(
        default=''
    )

    def execute(self, context):
        # form url
        url_base = 'https://www.youtube.com/results?'
        url_vars = ''
        if self.search:
            url_vars += 'search_query='
            if self.prefix:
                url_vars += self.prefix + ' '
            url_vars += self.search
            if self.sort_by_date:
                url_vars += '&sp=CAI%253D'
            if self.region:
                url_vars += '&lr=' + self.region
        url = url_base + url_vars
        bpy.ops.wm.url_open(
            'INVOKE_DEFAULT',
            url=url
        )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return bool(context.window_manager.youtube_search_vars.search)


def register():
    register_class(YOUTUBE_SEARCH_OT_search)


def unregister():
    unregister_class(YOUTUBE_SEARCH_OT_search)

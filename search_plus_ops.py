# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_search_plus

import bpy
from bpy.types import Operator
from bpy.props import StringProperty, BoolProperty
from bpy.utils import register_class, unregister_class


class SEARCH_PLUS_OT_search(Operator):
    bl_idname = 'search_plus.search'
    bl_label = 'Search'
    bl_description = 'Search in external sources'
    bl_options = {'UNDO'}

    def execute(self, context):
        search_vars = context.window_manager.search_plus_vars
        pref_vars = context.preferences.addons[__package__].preferences
        print(pref_vars.search_in)
        # form url
        # url_base = 'https://www.youtube.com/results?'
        # url_vars = ''
        # if self.search:
        #     url_vars += 'search_query='
        #     if self.prefix:
        #         url_vars += self.prefix + ' '
        #     url_vars += self.search
        #     if self.sort_by_date:
        #         url_vars += '&sp=CAI%253D'
        #     if self.region:
        #         url_vars += '&lr=' + self.region
        # url = url_base + url_vars
        # bpy.ops.wm.url_open(
        #     'INVOKE_DEFAULT',
        #     url=url
        # )
        return {'FINISHED'}

    # @classmethod
    # def poll(cls, context):
    #     return bool(context.window_manager.search_plus_vars.search_str)


def register():
    register_class(SEARCH_PLUS_OT_search)


def unregister():
    unregister_class(SEARCH_PLUS_OT_search)

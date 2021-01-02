# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_search_plus

import bpy
from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class SEARCH_PLUS_OT_search(Operator):
    bl_idname = 'search_plus.search'
    bl_label = 'Search'
    bl_description = 'Search in external sources'
    bl_options = {'UNDO'}

    def execute(self, context):
        search_vars = context.window_manager.search_plus_vars
        pref_vars = context.preferences.addons[__package__].preferences
        if 'GOOGLE' in pref_vars.search_in:
            # form url
            url_base = 'https://www.google.com/search?'
            url_vars = ''
            url_vars += 'newwindow=1'
            url_vars += '&q='
            if pref_vars.google_addition_words:
                url_vars += pref_vars.google_addition_words + ' '
            url_vars += search_vars.search_str
            url_vars = url_vars.replace(' ', '+')
            bpy.ops.wm.url_open(
                url=url_base + url_vars
            )
        if 'B_STACK_EXCHANGE' in pref_vars.search_in:
            url_base = 'https://blender.stackexchange.com/search?'
            url_vars = ''
            url_vars += 'q=' + search_vars.search_str
            if pref_vars.b_s_e_tags:
                tags_str = '%5B' + '%5D %5B'.join(pref_vars.b_s_e_tags.split(' ')) + '%5D'
                url_vars += ' ' + tags_str
            if pref_vars.b_s_e_answers:
                url_vars += ' ' + 'answers%3A' + str(pref_vars.b_s_e_answers)
            url_vars = url_vars.replace(' ', '+')
            bpy.ops.wm.url_open(
                url=url_base + url_vars
            )
        if 'YOUTUBE' in pref_vars.search_in:
            # form url
            url_base = 'https://www.youtube.com/results?'
            url_vars = ''
            url_vars += 'search_query='
            if pref_vars.youtube_addition_words:
                url_vars += pref_vars.youtube_addition_words + ' '
            url_vars += search_vars.search_str
            url_vars = url_vars.replace(' ', '+')
            if pref_vars.youtube_sort_by != 'EMPTY':
                url_vars += '&sp=' + pref_vars.youtube_sort_by
            bpy.ops.wm.url_open(
                url=url_base + url_vars
            )
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return bool(context.window_manager.search_plus_vars.search_str)


def register():
    register_class(SEARCH_PLUS_OT_search)


def unregister():
    unregister_class(SEARCH_PLUS_OT_search)

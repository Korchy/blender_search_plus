# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_search_plus

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class SEARCH_PLUS_PT_panel(Panel):
    bl_idname = 'SEARCH_PLUS_PT_panel'
    bl_label = 'Search Plus'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Search Plus'

    def draw(self, context):
        layout = self.layout
        search_vars = context.window_manager.search_plus_vars
        pref_vars = context.preferences.addons[__package__].preferences
        row = layout.row()
        # search field
        row.prop(data=search_vars, property='search_str', text='')
        # search button
        op = row.operator('search_plus.search', text='', icon='VIEWZOOM')
        # params
        row = layout.row()
        row.prop(data=pref_vars, property='search_in', expand=True)


def register():
    register_class(SEARCH_PLUS_PT_panel)


def unregister():
    unregister_class(SEARCH_PLUS_PT_panel)

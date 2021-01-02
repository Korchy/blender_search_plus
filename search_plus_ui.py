# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_search_plus

from bpy.types import Panel
from bpy.utils import register_class, unregister_class


class YOUTUBE_SEARCH_PT_panel(Panel):
    bl_idname = 'YOUTUBE_SEARCH_PT_panel'
    bl_label = 'YouTube Search'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_category = 'Search'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        op_vars = context.window_manager.youtube_search_vars
        row = layout.row()
        # search field
        row.prop(data=op_vars, property='search', text='')
        # search button
        op = row.operator('youtube_search.search', text='', icon='VIEWZOOM')
        op.search = op_vars.search
        op.prefix = op_vars.prefix
        op.sort_by_date = op_vars.sort_by_date
        op.region = op_vars.region
        # params
        row = layout.row()
        row.prop(data=op_vars, property='prefix')
        row.prop(data=op_vars, property='region')
        layout.prop(data=op_vars, property='sort_by_date')


def register():
    register_class(YOUTUBE_SEARCH_PT_panel)


def unregister():
    unregister_class(YOUTUBE_SEARCH_PT_panel)

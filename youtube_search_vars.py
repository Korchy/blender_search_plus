# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_youtube_search

import bpy
from bpy.props import StringProperty, BoolProperty, PointerProperty
from bpy.types import PropertyGroup, WindowManager
from bpy.utils import register_class, unregister_class


class YOUTUBE_SEARCH_vars(PropertyGroup):

    search: StringProperty(
        name='Search',
        default='',
        update=lambda self, context: self.on_update(context=context)
    )

    prefix: StringProperty(
        name='Prefix',
        default=''
    )

    sort_by_date: BoolProperty(
        name='Sort by date',
        default=False
    )

    region: StringProperty(
        name='Region',
        default=''
    )

    def on_update(self, context):
        bpy.ops.youtube_search.search(
            search=self.search,
            prefix=self.prefix,
            sort_by_date=self.sort_by_date,
            region=self.region
        )


def register():
    register_class(YOUTUBE_SEARCH_vars)
    WindowManager.youtube_search_vars = PointerProperty(type=YOUTUBE_SEARCH_vars)


def unregister():
    del WindowManager.youtube_search_vars
    unregister_class(YOUTUBE_SEARCH_vars)

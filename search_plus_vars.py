# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_search_plus

import bpy
from bpy.props import StringProperty, PointerProperty
from bpy.types import PropertyGroup, WindowManager
from bpy.utils import register_class, unregister_class


class SEARCH_PLUS_vars(PropertyGroup):

    search_str: StringProperty(
        name='Search',
        default=''
    )


def register():
    register_class(SEARCH_PLUS_vars)
    WindowManager.search_plus_vars = PointerProperty(type=SEARCH_PLUS_vars)


def unregister():
    del WindowManager.search_plus_vars
    unregister_class(SEARCH_PLUS_vars)

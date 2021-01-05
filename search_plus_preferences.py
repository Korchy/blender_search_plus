# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/blender_search_plus

from bpy.types import AddonPreferences
from bpy.props import EnumProperty, StringProperty, IntProperty
from bpy.utils import register_class, unregister_class


class SEARCH_PLUS_preferences(AddonPreferences):
    bl_idname = __package__

    search_in: EnumProperty(
        name='Search in',
        items=[
            ('GOOGLE', 'Google', 'Google'),
            ('B_STACK_EXCHANGE', 'Blender Stack Exchange', 'Blender Stack Exchange'),
            ('YOUTUBE', 'YouTube', 'YouTube')
        ],
        options={'ENUM_FLAG'},
        default={'GOOGLE', 'B_STACK_EXCHANGE', 'YOUTUBE'}
    )

    youtube_sort_by = EnumProperty(
        name='Sort by',
        items=[
            ('EMPTY', '', 'No sort'),
            ('CAISAhAB', 'Upload date', 'Upload date'),
            ('CAASAhAB', 'Relevance', 'Relevance'),
            ('CAMSAhAB', 'View count', 'View count'),
            ('CAESAhAB', 'Rating', 'Rating')
        ],
        default='EMPTY'
    )

    youtube_addition_words = StringProperty(
        name='Addition words',
        default='blender'
    )

    b_s_e_tags = StringProperty(
        name='Tags',
        default=''
    )

    b_s_e_answers = IntProperty(
        name='Minimum answers',
        subtype='UNSIGNED',
        min=0,
        default=0
    )

    google_addition_words = StringProperty(
        name='Addition words',
        default='blender'
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text='Search in:')
        row = layout.row()
        row.prop(self, 'search_in')
        # Google preferences
        box = layout.box()
        box.label(text='Google')
        box.prop(self, 'google_addition_words')
        # Blender Stack Exchange preferences
        box = layout.box()
        box.label(text='Blender Stack Exchange')
        box.prop(self, 'b_s_e_tags')
        box.prop(self, 'b_s_e_answers')
        # YouTube preferences
        box = layout.box()
        box.label(text='YouTube')
        box.prop(self, 'youtube_sort_by')
        box.prop(self, 'youtube_addition_words')


def register():
    register_class(SEARCH_PLUS_preferences)


def unregister():
    unregister_class(SEARCH_PLUS_preferences)

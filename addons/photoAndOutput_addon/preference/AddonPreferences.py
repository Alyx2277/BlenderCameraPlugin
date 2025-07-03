import os

import bpy
from bpy.props import StringProperty, IntProperty, BoolProperty
from bpy.types import AddonPreferences

from ..config import __addon_name__


class ExampleAddonPreferences(AddonPreferences):
    # this must match the add-on name (the folder name of the unzipped file)
    bl_idname = __addon_name__

    # https://docs.blender.org/api/current/bpy.props.html
    # The name can't be dynamically translated during blender programming running as they are defined
    # when the class is registered, i.e. we need to restart blender for the property name to be correctly translated.
    number: bpy.props.IntProperty(
        name="Number",
        default=0,
        min=0
    )
    filepath: bpy.props.StringProperty(
        name="File Path",
        subtype='FILE_PATH'
    )
    boolean: bpy.props.BoolProperty(
        name="Boolean",
        default=False
    )
    output_fps: bpy.props.IntProperty(
        name="FPS",
        default=24
    )
    output_resolution_x: bpy.props.IntProperty(
        name="Resolution X",
        default=1920,
        min=1
    )
    output_resolution_y: bpy.props.IntProperty(
        name="Resolution Y",
        default=1080,
        min=1
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "number")
        layout.prop(self, "filepath")
        layout.prop(self, "boolean")
        layout.prop(self, "output_start_frame")
        layout.prop(self, "output_end_frame")
        layout.prop(self, "output_resolution_x")
        layout.prop(self, "output_resolution_y")

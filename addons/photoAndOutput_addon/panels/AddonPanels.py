import bpy

from ..config import __addon_name__
from ..operators.AddonOperators import RecordAnimationAsPNG
from ....common.i18n.i18n import i18n
from ....common.types.framework import reg_order


class BasePanel(object):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "ExampleAddon"

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return True


@reg_order(0)
class ExampleAddonPanel(BasePanel, bpy.types.Panel):
    bl_label = "Example Addon Side Bar Panel"
    bl_idname = "SCENE_PT_sample"

    def draw(self, context: bpy.types.Context):
        addon_prefs = context.preferences.addons[__addon_name__].preferences

        layout = self.layout

        # 添加输出帧数设置
        layout.prop(addon_prefs, "output_fps")
        # 添加输出分辨率设置
        layout.separator()
        layout.prop(addon_prefs, "output_resolution_x")
        layout.prop(addon_prefs, "output_resolution_y")
        # 添加输出帧范围设置
        layout.separator()
        layout.prop(addon_prefs, "output_start_frame")
        layout.prop(addon_prefs, "output_end_frame")
        layout.prop(addon_prefs, "output_step_frame")

        # 添加新按钮
        layout.operator(RecordAnimationAsPNG.bl_idname, text="Record Animation as PNG")

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return True


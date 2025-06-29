import bpy

from ..config import __addon_name__
from ..operators.AddonOperators import ExampleOperator
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

        layout.label(text=i18n("Example Functions") + ": " + str(addon_prefs.number))
        layout.prop(addon_prefs, "filepath")
        layout.separator()

        row = layout.row()
        row.prop(addon_prefs, "number")
        row.prop(addon_prefs, "boolean")

        layout.operator(ExampleOperator.bl_idname)

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return True


# This panel will be drawn after ExampleAddonPanel since it has a higher order value
@reg_order(1)
class ExampleAddonPanel2(BasePanel, bpy.types.Panel):
    bl_label = "camera_list"
    bl_idname = "SCENE_PT_camera_list"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Camera Addon"

    def draw(self, context: bpy.types.Context):
        layout = self.layout

        # 打印所有摄像头的按钮
        layout.operator("camera.print_all_cameras", text="打印所有摄像头")

        layout.separator()

        # 获取场景中所有摄像头
        cameras = [obj for obj in bpy.data.objects if obj.type == 'CAMERA']

        if not cameras:
            layout.label(text="场景中没有摄像头")
        else:
            for camera in cameras:
                row = layout.row()
                row.label(text=camera.name)

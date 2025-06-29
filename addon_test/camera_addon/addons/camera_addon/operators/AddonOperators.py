import bpy

from ..config import __addon_name__
from ..preference.AddonPreferences import ExampleAddonPreferences


# This Example Operator will scale up the selected object
class ExampleOperator(bpy.types.Operator):
    """打印当前场景中所有摄像头"""
    bl_idname = "camera.print_all_cameras"
    bl_label = "Print All Cameras"

    # 确保在操作之前备份数据，用户撤销操作时可以恢复
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.scene is not None

    def execute(self, context: bpy.types.Context):
        cameras = [obj for obj in context.scene.objects if obj.type == 'CAMERA']
        if not cameras:
            self.report({'INFO'}, "场景中没有摄像头")
        else:
            for camera in cameras:
                print(f"摄像头名称: {camera.name}")
            self.report({'INFO'}, f"打印了 {len(cameras)} 个摄像头")
        return {'FINISHED'}

import bpy

from ..config import __addon_name__
from ..preference.AddonPreferences import ExampleAddonPreferences


# This Example Operator will scale up the selected object
class ExampleOperator(bpy.types.Operator):
    '''选中特定摄像头，执行当前模型动画，并记录成 PNG 序列帧导出'''
    bl_idname = "camera.record_animation_png"
    bl_label = "Record Animation as PNG"

    # 确保在操作之前备份数据，用户撤销操作时可以恢复
    bl_options = {'REGISTER', 'UNDO'}

    camera_name: bpy.props.StringProperty(
        name="Camera Name",
        description="要使用的摄像头名称",
        default=""
    )

    output_path: bpy.props.StringProperty(
        name="Output Path",
        description="PNG 序列帧的输出路径",
        default="",
        subtype='DIR_PATH'
    )

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.scene is not None

    def execute(self, context: bpy.types.Context):
        # 获取指定名称的摄像头
        camera = bpy.data.objects.get(self.camera_name)
        if not camera or camera.type != 'CAMERA':
            self.report({'ERROR'}, "未找到指定的摄像头")
            return {'CANCELLED'}

        # 设置渲染引擎为 Cycles
        context.scene.render.engine = 'CYCLES'
        # 设置活动摄像头
        context.scene.camera = camera

        # 设置输出路径
        context.scene.render.filepath = self.output_path
        # 设置输出格式为 PNG
        context.scene.render.image_settings.file_format = 'PNG'

        # 获取动画的起始和结束帧
        start_frame = context.scene.frame_start
        end_frame = context.scene.frame_end

        # 渲染并保存每帧
        for frame in range(start_frame, end_frame + 1):
            context.scene.frame_set(frame)
            bpy.ops.render.render(write_still=True)

        self.report({'INFO'}, f"动画已成功导出为 PNG 序列帧到 {self.output_path}")
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

class RecordAnimationAsPNG(bpy.types.Operator):
    """选中特定摄像头，执行当前模型动画，并记录成 PNG 序列帧导出"""
    bl_idname = "camera.record_animation_png"
    bl_label = "Record Animation as PNG"

    # 确保在操作之前备份数据，用户撤销操作时可以恢复
    bl_options = {'REGISTER', 'UNDO'}

    camera_name: bpy.props.StringProperty(
        name="Camera Name",
        description="要使用的摄像头名称",
        default=""
    )

    output_path: bpy.props.StringProperty(
        name="Output Path",
        description="PNG 序列帧的输出路径",
        default="",
        subtype='DIR_PATH'
    )

    @classmethod
    def poll(cls, context: bpy.types.Context):
        return context.scene is not None

    def execute(self, context: bpy.types.Context):
        # 获取指定名称的摄像头
        camera = bpy.data.objects.get(self.camera_name)
        if not camera or camera.type != 'CAMERA':
            self.report({'ERROR'}, "未找到指定的摄像头")
            return {'CANCELLED'}

        # 设置渲染引擎为 Cycles
        context.scene.render.engine = 'CYCLES'
        # 设置活动摄像头
        context.scene.camera = camera

        # 获取动画的起始和结束帧
        start_frame = context.scene.frame_start
        end_frame = context.scene.frame_end

        for frame in range(start_frame, end_frame + 1):
            # 计算相对帧号，从 1 开始
            relative_frame = frame - start_frame + 1
            # 构建输出文件路径，格式为 fpsX.png
            output_file_path = f"{self.output_path}fps{relative_frame}.png"
            context.scene.render.filepath = output_file_path
            # 设置输出格式为 PNG
            context.scene.render.image_settings.file_format = 'PNG'

            context.scene.frame_set(frame)
            bpy.ops.render.render(write_still=True)

        self.report({'INFO'}, f"动画已成功导出为 PNG 序列帧到 {self.output_path}")
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)
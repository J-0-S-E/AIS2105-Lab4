from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    rectify_node = Node(
        package='image_proc',
        executable='rectify_node',
        name='rectify_node',
        output='screen'
    )

    gaussian_blur_node = Node(
        package='camera_pipeline',
        executable='gaussian_blur',
        name='gaussian_blur',
        output='screen',
        remappings=[
            ('image_raw', 'image_rect'),
            ('output_image', 'image_blurred'),
        ]
    )

    canny_edge_node = Node(
        package='camera_pipeline',
        executable='canny_edge',
        name='canny_edge',
        output='screen',
        remappings=[
            ('image_raw', 'image_blurred'),
        ]
    )

    return LaunchDescription([
        rectify_node,
        gaussian_blur_node,
        canny_edge_node,
    ])
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    rectify_node = Node(
        package='image_proc',
        executable='rectify_node',
        name='rectify_node',
        output='screen'
    )

    return LaunchDescription([
        rectify_node
    ])
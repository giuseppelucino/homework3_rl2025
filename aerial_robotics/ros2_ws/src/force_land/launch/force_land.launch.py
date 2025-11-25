from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    force_land_node = Node(
        
        package='force_land',
        
        
        executable='force_land',
        
        
        name='force_land_monitor',
        
    
        output='screen',
        

    )

    return LaunchDescription([
        force_land_node,
    ])




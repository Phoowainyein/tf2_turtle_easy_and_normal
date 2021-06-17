#! /usr/bin/python3

import rospy
import tf_conversions

import tf2_ros
import geometry_msgs.msg
import turtlesim.msg

def handle_turtle_pose(msg,turtlename):
    br =tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()
# Give the transform being published a timestamp
    t.header.stamp = rospy.Time.now()
    # Set the name of the parent link
    t.header.frame_id = "world"
     # Set the name of the child node
    t.child_frame_id = turtlename
    # Broadcast the turtle's translation and rotation
    # Published as a transform from frame "world" to frame "turtleX"
    # Copy the information from the 3D turtle post into the
    # 3D transform.
    t.transform.translation.x =msg.x
    t.transform.translation.y =msg.y
    t.transform.translation.z=0.0
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]
# Pass in the transform and send it
    br.sendTransform(t)

if __name__=='__main__':
    rospy.init_node('tf2_turtle_broadcaster')
    # This node takes a single parameter "turtle", 
    # which specifies a turtle name, e.g. "turtle1" or "turtle2"
    turtlename =rospy.get_param('~turtle')
    # The node subscribes to topic "turtleX/pose" 
    # and runs function handle_turtle_pose on every incoming message.
    rospy.Subscriber('/%s/pose' % turtlename, turtlesim.msg.Pose,handle_turtle_pose,turtlename)

    rospy.spin()

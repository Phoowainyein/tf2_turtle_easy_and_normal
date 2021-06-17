#! /usr/bin/python3

import rospy
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv
import math

if __name__=='__main__':
    rospy.init_node('tf2_turtle_listener')

    tf_buffer = tf2_ros.Buffer()
    listener=tf2_ros.TransformListener(tf_buffer)

    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn',turtlesim.srv.Spawn)
    turtle_name = rospy.get_param('turtle','turtle2')
    spawner(4,2,0,turtle_name)

    turtle_vel = rospy.Publisher('%s/cmd_vel' % turtle_name, geometry_msgs.msg.Twist, queue_size=1)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            trans = tf_buffer.lookup_transform(turtle_name, 'turtle1', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue


        msg = geometry_msgs.msg.Twist()
 
        msg.angular.z = 4 * math.atan2(trans.transform.translation.y, trans.transform.translation.x)
        msg.linear.x = 0.2 * math.sqrt(trans.transform.translation.x ** 2 + trans.transform.translation.y ** 2) 
        turtle_vel.publish(msg) 
        rate.sleep()

        
#    1 #!/usr/bin/env python  
#    2 import rospy
#    3 
#    4 import math
#    5 import tf2_ros
#    6 import geometry_msgs.msg
#    7 import turtlesim.srv
#    8 
#    9 if __name__ == '__main__':
#   10     rospy.init_node('tf2_turtle_listener')
#   11 
#   12     tfBuffer = tf2_ros.Buffer()
#   13     listener = tf2_ros.TransformListener(tfBuffer)
#   14 
#   15     rospy.wait_for_service('spawn')
#   16     spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
#   17     turtle_name = rospy.get_param('turtle', 'turtle2')
#   18     spawner(4, 2, 0, turtle_name)
#   19 
#   20     turtle_vel = rospy.Publisher('%s/cmd_vel' % turtle_name, geometry_msgs.msg.Twist, queue_size=1)
#   21 
#   22     rate = rospy.Rate(10.0)
#   23     while not rospy.is_shutdown():
#   24         try:
#   25             trans = tfBuffer.lookup_transform(turtle_name, 'turtle1', rospy.Time())
#   26         except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
#   27             rate.sleep()
#   28             continue
#   29 
#   30         msg = geometry_msgs.msg.Twist()
#   31 
#   32         msg.angular.z = 4 * math.atan2(trans.transform.translation.y, trans.transform.translation.x)
#   33         msg.linear.x = 0.5 * math.sqrt(trans.transform.translation.x ** 2 + trans.transform.translation.y ** 2)
#   34 
#   35         turtle_vel.publish(msg)
#   36 
#   37         rate.sleep()
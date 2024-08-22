#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen


prev_pose = {
    "x":5.5,
    "y":5.5
}

def set_turtle_pen(r, g, b, width=4, off=False):
    try:
        set_pen = rospy.ServiceProxy("/turtle1/set_pen", SetPen)
        response = set_pen(r, g, b, width, off)
    except rospy.ServiceException as e:
        rospy.logwarn(e)



def pose_callback(msg: Pose):
    cmd = Twist()
    if msg.x < 2 or msg.x > 9 or msg.y < 2 or msg.y > 9:
        cmd.linear.x = 1.0
        cmd.angular.z = 0.7
    else:
        cmd.linear.x = 5.0
        cmd.angular.z = 0.0
    
    if msg.x < 5.5:
        set_turtle_pen(255, 0, 0)
    else:
        set_turtle_pen(0, 255, 0)
        
    prev_pose["x"], prev_pose["y"] = msg.x, msg.y 
    pub.publish(cmd)

if __name__=="__main__":
    rospy.init_node("turtle_controller")
    rospy.loginfo("Node has started!")
    rospy.wait_for_service("/turtle1/set_pen")
    

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)

    rospy.spin()
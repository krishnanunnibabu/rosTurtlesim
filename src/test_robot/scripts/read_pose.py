#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_callback(msg: Pose):
    rospy.loginfo(f"({round(msg.x, 3)}, {round(msg.y, 3)})")

if __name__=="__main__":
    rospy.init_node("read_pose")
    rospy.loginfo("Node has started!")

    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)

    rospy.spin()
    rospy.loginfo("Exiting node...")
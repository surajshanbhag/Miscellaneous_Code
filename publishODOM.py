import rospy
from geometry_msgs.msg import Twist, Pose, Vector3,Quaternion, Point, TransformStamped
import geometry_msgs.msg
from nav_msgs.msg import Odometry
import socket
import subprocess,sys
global s,reply

def odom_callback(data):
    global s,reply
    print data.header.stamp
    output=str(data.header.stamp)
    if reply == "OK":
        c.send(output+"$");
    if not reply:
        sys.exit(0)
    reply = c.recv(4096)
    print(output+"\t :"+reply+"\n")

if __name__ == '__main__':
    global s,reply

    reply="OK"
    s = socket.socket()
    print "Socket successfully created"
    port = 12345
    s.bind(('', port))
    print "socket binded to %s" %(port)
    s.listen(5)
    print "socket is listening"
    c, addr = s.accept()
    print 'Got connection from', addr
    rospy.init_node('publishOdom',anonymous=True)
    rospy.Subscriber("/husky_velocity_controller/odom", Odometry, odom_callback)
    rospy.spin()


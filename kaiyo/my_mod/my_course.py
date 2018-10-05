#coding: utf-8
import time
import sys
# マルチタスク
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data, log
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca
from my_balance import yaw, go_yaw, go_yaw_rot, diving, diving_while, go_yaw_simulator
from my_rc import t10j
from my_check import operation_check, status_check, my_exit
from my_gpio import led_red, led_green, led_yellow, led_off


# -----------------------------------------------------------------------------




def test(set_speed, set_time):
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(80)
    time.sleep(3)
    yaw(0)

    # Uターン地点まで行く
    print "go_yaw"
    led_green()
    go_yaw(set_speed, 0, set_time)

    # 慣性で流れるのを停止
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-50)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(60)
    time.sleep(2)

    # Uターン
    print "yaw"
    yaw(100)

    # スタート地点まで行く
    print "go_yaw"
    led_green()
    go_yaw(set_speed-2, 100, set_time)


    # 浮上
    print "up"
    # diving_while(20)
    up_down(80)
    time.sleep(3)


    # Uターン
    print "yaw"
    yaw(0)

    led_red()
    stop()




def test_rot(set_speed, set_rot):
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(80)
    time.sleep(3)
    yaw(0)

    # Uターン地点まで行く
    print "go_yaw"
    led_green()
    # go_yaw_rot(set_speed, 0, set_rot)
    go_yaw_simulator(set_speed, 0, set_rot)

    # 慣性で流れるのを停止
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-50)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(60)
    time.sleep(2)

    # Uターン
    print "yaw"
    yaw(100)

    # スタート地点まで行く
    print "go_yaw"
    led_green()
    # go_yaw_rot(set_speed, 100, set_rot)
    go_yaw_simulator(set_speed, 100, set_rot)


    # 慣性で流れるのを停止
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-50)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    led_off()
    # diving_while(20)
    up_down(80)
    time.sleep(3)


    # Uターン
    print "yaw"
    led_red()
    yaw(0)

    stop()

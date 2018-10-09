#coding: utf-8
import time
import sys
# マルチタスク
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data, log
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca
from my_balance import yaw, go_yaw_time, go_yaw_rot, diving, diving_while, go_yaw_onoff
from my_rc import t10j
from my_check import operation_check, status_check, my_exit
from my_gpio import led_red, led_green, led_yellow, led_off
from my_state_write import state_write

# -----------------------------------------------------------------------------


"""
def test(set_speed, set_time):
def test_rot(set_speed, set_rot):
def test_rot_onoff(set_speed, set_rot):
def course_ver1(set_speed, set_rot):
def course_ver2(set_speed, set_rot):
def course_data_picking(set_speed, set_rot):
"""


def test(set_speed, set_time):
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(80)
    time.sleep(3)
    yaw(0, set_diving=False)

    # Uターン地点まで行く
    print "go_yaw"
    led_green()
    go_yaw_time(set_speed, 0, set_time, set_diving=80)

    # 慣性で流れるのを停止
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-30)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(60)
    time.sleep(2)

    # Uターン
    print "yaw"
    yaw(100, set_diving=False)

    # スタート地点まで行く
    print "go_yaw"
    led_green()
    go_yaw_time(set_speed-2, 100, set_time, set_diving=80)


    # 浮上
    print "up"
    # diving_while(20)
    up_down(80)
    time.sleep(3)


    # Uターン
    print "yaw"
    yaw(0, set_diving=False)

    led_red()
    stop()


# -----------------------------------------------------------------------------


def test_rot(set_speed, set_rot):
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(80)
    time.sleep(3)
    yaw(0, set_diving=False)

    # Uターン地点まで行く
    print "go_yaw"
    led_green()
    go_yaw_rot(set_speed, 0, set_rot, set_diving=80)

    # 慣性で流れるのを停止
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-30)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(60)
    time.sleep(4)

    # Uターンの補助
    spinturn(30)
    time.sleep(1.2)
    stop()

    # Uターン
    print "yaw"
    yaw(100, set_diving=False)
    led_red()
    time.sleep(0.5)
    print "yaw"
    yaw(100, set_diving=False)

    # スタート地点まで行く
    print "go_yaw"
    led_green()
    go_yaw_rot(set_speed, 100, set_rot)


    # 慣性で流れるのを停止
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-30)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    led_off()
    # diving_while(20)
    up_down(80)
    time.sleep(3)

    # Uターンの補助
    spinturn(20)
    time.sleep(1)
    stop()

    # Uターン
    print "yaw"
    led_red()
    yaw(0, set_diving=False)

    stop()


# -----------------------------------------------------------------------------


def test_rot_onoff(set_speed, set_rot):
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(80)
    time.sleep(3)
    yaw(0, set_diving=False)

    # Uターン地点まで行く
    print "go_yaw"
    led_green()
    # go_yaw_rot(set_speed, 0, set_rot)
    go_yaw_onoff(set_speed, 0, set_rot, set_diving=80)

    # 慣性で流れるのを停止
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-30)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(60)
    time.sleep(2)

    # Uターン
    print "yaw"
    yaw(100, set_diving=False)

    # スタート地点まで行く
    print "go_yaw"
    led_green()
    # go_yaw_rot(set_speed, 100, set_rot)
    go_yaw_onoff(set_speed, 100, set_rot, set_diving=80)


    # 慣性で流れるのを停止
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-30)
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
    yaw(0, set_diving=False)

    stop()


# -----------------------------------------------------------------------------


def course_ver1(set_speed, set_rot):
    stop()

    # 浮上
    state_write("up")
    print "up"
    # diving_while(20)
    up_down(80)
    time.sleep(3)
    yaw(0, set_diving=False)

    # Uターン地点まで行く
    state_write("go_yaw")
    print "go_yaw"
    led_green()
    go_yaw_rot(set_speed, 0, set_rot, set_diving=60)
    # go_yaw_rot(set_speed, 0, set_rot, set_diving=False)

    # 慣性で流れるのを停止
    state_write("stop U")
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    # 浮上
    state_write("up")
    print "up"
    # diving_while(20)
    up_down(60)
    time.sleep(4)

    # Uターンの補助
    spinturn(30)
    time.sleep(1)
    stop()

    # Uターン
    state_write("yaw")
    print "yaw"
    yaw(100, set_diving=False)
    led_red()
    time.sleep(0.5)
    print "yaw"
    yaw(100, set_diving=False)

    # スタート地点まで行く
    state_write("go_yaw")
    print "go_yaw"
    led_green()
    go_yaw_rot(set_speed, 100, set_rot, set_diving=60)
    # go_yaw_rot(set_speed, 100, set_rot, set_diving=False)


    # 慣性で流れるのを停止
    stop()
    led_off()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    # 浮上
    state_write("up")
    print "up"
    led_off()
    # diving_while(20)
    up_down(80)
    time.sleep(3)


    state_write("end")
    stop()


# -----------------------------------------------------------------------------


def course_ver2(set_speed, set_rot):
    state_write("\ncourse_ver2 START")
    stop()

    # 浮上
    print "up"
    state_write("up")
    # diving_while(20)
    # yaw(0, set_diving=1)
    up_down(80)
    time.sleep(3)
    yaw(0, set_diving=False)

    # Uターン地点まで行く
    print "go_yaw"
    state_write("go_yaw")
    led_green()
    go_yaw_rot(set_speed, 0, set_rot, set_diving=90)
    led_off()

    # 慣性で流れるのを停止
    stop()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    state_write("up")
    # diving_while(20)
    up_down(60)
    time.sleep(4)

    # Uターン
    print "yaw"
    state_write("yaw")
    # yaw(100, set_diving=1)
    yaw(100, set_diving=False)

    # スタート地点まで行く
    print "go_yaw"
    state_write("go_yaw")
    led_green()
    # go_yaw_rot(set_speed, 100, set_rot)
    go_yaw_rot(set_speed, 100, set_rot, set_diving=90)
    led_off()

    # 慣性で流れるのを停止
    stop()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    # 浮上
    print "up"
    state_write("up")
    led_off()
    # diving_while(20)
    up_down(60)
    time.sleep(4)

    state_write("END")
    stop()

    my_exit()


# -----------------------------------------------------------------------------


def course_ver3(set_speed, set_rot):
    state_write("\ncourse_ver3 START")
    stop()

    # 浮上
    diving_while(30)
    yaw(0, set_diving=20)

    # 海上航行
    led_red()
    go_yaw_rot(set_speed, 0, 40, set_diving=20)
    led_off()

    stop()
    diving_while(80)

    # Uターン地点まで行く
    led_green()
    go_yaw_rot(set_speed, 0, 50, set_diving=80)
    led_off()

    # 慣性で流れるのを停止
    stop()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    # 浮上してUターン
    diving_while(30)
    yaw(100, set_diving=20)

    # スタート地点まで行く
    led_green()
    go_yaw_rot(set_speed, 100, 50, set_diving=80)
    led_off()

    stop()
    diving_while(30)

    # 海上航行
    led_red()
    go_yaw_rot(set_speed, 100, 40, set_diving=30)
    led_off()

    # 慣性で流れるのを停止
    stop()
    time.sleep(0.5)
    go_back(-20)
    time.sleep(1)
    stop()

    # 浮上
    diving_while(20)

    stop()

    my_exit()

# -----------------------------------------------------------------------------


def course_data_picking(set_speed, set_rot):
    stop()

    # 浮上
    print "up"
    # diving_while(20)
    # yaw(0, set_diving=1)
    up_down(80)
    time.sleep(3)
    yaw(0, set_diving=False)

    # Uターン地点まで行く
    print "go_yaw"
    led_green()
    go_yaw_rot(set_speed, 0, set_rot, set_diving=80)
    led_off()

    stop_go_back()

    # 浮上
    print "up"
    # diving_while(20)
    up_down(60)
    time.sleep(4)

    stop()

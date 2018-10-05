#coding: utf-8
import time
import sys
# マルチタスク
sys.path.append("/kaiyo/my_mod")
from my_get_serial import get_data, send_data, log
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, br_xr, go_back_each, up_down_each, spinturn_each, spinturn_meca
from my_balance import yaw, go_yaw, go_yaw_rot, diving, diving_while, go_yaw_simulator, go_yaw_onoff
from my_rc import t10j
from my_check import operation_check, status_check, my_exit
from my_gpio import led_red, led_green, led_yellow, led_off
from my_course import test, test_rot


# -----------------------------------------------------------------------------


def mode_set():
    # 念のためモーターstop
    stop()
    # センサー初期化
    send_data("reboot")
    # マシンの状態をチェック
    status_check(set_lipoC2=7.5, set_lipoC3S3=12)
    # 待機状態のLEDをセット
    led_red()


    # textにlogを残すか？
    log()

    # 動作チェックするか？
    # operation_check()

    # リードスイッチでスタート
    data =  get_data("all")
    # print data
    while data["mgs"] == 0:
        data =  get_data("all")
        print data["mgs"]
        print "Ready !!"

    # センサー初期化
    send_data("reboot")

    # カウントダウン
    for cnt in range(6, 0, -1):
        led_red()
        print cnt
        time.sleep(0.5)
        led_off()
        time.sleep(0.5)

    print "Go !!"
    led_yellow()




def my_main():
    # センサーデータ取得
    data = get_data("all")
    # print data
    # test(30, 9)
    # test_rot(30, 100)
    # test_rot(40, 100)
    # go_yaw_simulator(30, 0, 200)
    go_yaw_onoff(30, 0, 200)
    # yaw(0)
    # go_yaw(80, 0, 30)
    # diving_while(1)
    # go_back(10)
    # up_down_each(80,0)
    # diving(80)



# -------------------------------------------------------------------
if __name__ == '__main__':
    try:
        # 初期設定 and チェック
        send_data("reboot")
        # mode_set()
        while True:
            # 予期せぬエラーが発生した時の処理
            try:
                # Ctrl-cを押したときの処理
                try:
                    # メインのプログラム
                    # ----------------------------------------
                    my_main()
                    # break
                    # ----------------------------------------
                except KeyboardInterrupt as e:
                    # Ctrl-cを押したときの処理
                    print "\nCtrl-c!!"
                    my_exit()
            except Exception as e:
                # 予期せぬエラーが発生した時の処理
                # stop()
                print "\nError =",e
                print "Error!!!!!!!!!!!!!!!!!!!!!!!"
                led_green()
                time.sleep(0.05)
                led_off()
                time.sleep(0.05)

    except KeyboardInterrupt as e:
        print "\nCtrl-c!!"
        # プログラムを終了するときの処理
        my_exit()

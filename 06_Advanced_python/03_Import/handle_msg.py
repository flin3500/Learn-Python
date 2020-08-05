from common import RECV_DATA_LIST
# from common import HANDLE_FLAG
import common

def handle_data():
    """test RECV_DATA_LIST"""
    print("--->handle_data")
    for i in RECV_DATA_LIST:
        print(i)

    # global HANDLE_FLAG
    # HANDLE_FLAG = True
    common.HANDLE_FLAG = True

def test_handle_data():
    """test if HANDLE_FLAG become True"""
    print("--->test_handle_data")
    # if HANDLE_FLAG:
    if common.HANDLE_FLAG:
        print("=====finish====")
    else:
        print("=====not finish====")
from common import RECV_DATA_LIST
# from common import HANDLE_FLAG
import common


def recv_msg():
    """add data to RECV_DATA_LIST"""
    print("--->recv_msg")
    for i in range(5):
        RECV_DATA_LIST.append(i)


def test_recv_data():
    """test RECV_DATA_LIST"""
    print("--->test_recv_data")
    print(RECV_DATA_LIST)


def recv_msg_next():
    """if finish, receive other data"""
    print("--->recv_msg_next")
    # if HANDLE_FLAG:
    if common.HANDLE_FLAG:
        print("------finish, receive other data----")
    else:
        print("------still not finish, waiting------")
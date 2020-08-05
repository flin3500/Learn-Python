from recv_msg import *
from handle_msg import *


def main():
    # 1. receive message
    recv_msg()
    # 2. test if receive
    test_recv_data()
    # 3. if finish, receive other data
    recv_msg_next()
    # 4. handle data
    handle_data()
    # 5. test if finish handle
    test_handle_data()
    # 6. if finish, receive other data
    recv_msg_next()


if __name__ == "__main__":
    main()
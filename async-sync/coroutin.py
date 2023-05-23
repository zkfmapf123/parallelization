def hello_friends():
    """
        normal generator
    """
    yield "hello leedonggyu"
    yield "hello limjeahyock"
    yield "hello kimboyun"


def hello_friends_use_coroutin():
    while True:
        r = yield "hello leedonggyu"
        yield r


if __name__ == "__main__":
    """ 
        Corouting:
            - 특정 지점에서 함수를 일시정지하고, 다시 시작하는 개념
            - 단일 스레드내에서 협동 멀티태스킹을 가능하게 함
            - 현재 실행중인 작업을 중단하고 다른 함수(코루틴) 실행되도록 허용 (협동 멀티태스킹)
    """

    # for loop use generator
    # for friend in hello_friends():
    #     print(friend)

    # friend = hello_friends()
    # print(next(friend))
    # print(next(friend))
    # print(next(friend))
    # print(next(friend))

    friend = hello_friends_use_coroutin()
    print(next(friend))
    print(friend.send("limjeahock"))
    print(next(friend))
    print(friend.send("kimboyoun"))
    print(next(friend))

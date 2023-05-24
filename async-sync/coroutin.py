def hello_friends():
    """
        normal generator
    """
    yield "hello leedonggyu"
    yield "hello limjeahyock"
    yield "hello kimboyun"
    return "Done"


def hello_friends_use_coroutin():
    """
        코루틴 형태
    """
    while True:
        r = yield "hello leedonggyu"
        yield r


def hello_friends_use_coroutin_from():
    """
        코루틴 형태: 
            from 절을 사용해서 다른 Generator를 사용
    """

    while True:
        r = yield from hello_friends()
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

    # friend = hello_friends_use_coroutin()
    # print(next(friend))
    # print(friend.send("limjeahock"))
    # print(next(friend))
    # print(friend.send("kimboyoun"))

    friend = hello_friends_use_coroutin_from()
    print(next(friend))
    print(next(friend))
    print(next(friend))
    print(next(friend))  # None -> Done
    print(next(friend))  # 다시 반복
    print(next(friend))
    print(next(friend))
    print(next(friend))  # None -> Done

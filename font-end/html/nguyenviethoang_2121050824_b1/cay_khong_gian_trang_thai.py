# xây dựng các trạng thái đơn
# của môi trường tác nghiệp
class Node:
    def __init__(self, status) -> None:
        self._status = status
        self._parent = None
        # self._left = None
        # self._right = None


# Cây không gian trạng thái
class space:
    def __init__(self, root) -> None:
        self._root       


# Định nghĩa bài toán
class Problem:
    def __init__(self,initial,target,action, statues, strategy,space) -> None:
        self._initial = initial
        self._target = target
        self._action = action
        self._statuses = statues
        self._strategy = strategy
        self._space = space
        
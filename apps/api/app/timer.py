import threading
import time
from collections.abc import Callable


class RepeatedTimer[**P]:
    def __init__(
        self,
        interval: int,
        function: Callable[P, None],
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> None:
        self._timer: threading.Timer | None = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.next_call = time.time()
        self.start()

    def _run(self) -> None:
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self) -> None:
        if not self.is_running:
            self.next_call += self.interval
            self._timer = threading.Timer(
                self.next_call - time.time(),
                self._run,
            )
            self._timer.daemon = True
            self._timer.start()
            self.is_running = True

    def stop(self) -> None:
        if self._timer is not None:
            self._timer.cancel()
        self.is_running = False

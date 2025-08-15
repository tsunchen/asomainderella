import collections
import time
import heapq
import math

class OverLoop:

    __slots__ = ( '_stopping', '_scheduled', '_ready' )

    def __init__(self):
        self._ready = collections.deque()
        self._scheduled = []
        self._stopping = False

    def call_soon(self, callback, *args):
        self._ready.append((callback, args))

    def call_later(self, delay_metric, callback, *args):
        t = time.time() + delay_metric
        heapq.heappush(self._scheduled, (t, callback, args))
        # heapq.heappush(self._schedule, delay_metric)

    def stop(self):
        self._stopping = True

    def run_forever(self):
        while True:
            self.run_once()
            if self._stopping:
                break

    def run_once(self):
        # self.aview(self._schedule)
        now = time.time()
        if self._scheduled[0][0] < now:
            _, cb, args = heapq.heappop(self._scheduled)
            self._ready.append((cb, args))
        num = len(self._ready)
        for i in range(num):
            cb, args = self._ready.popleft()
            cb(*args)

    def aview(self, scheduled, fill = ' ', total_width = 64):
        from io import StringIO
        output = StringIO()
        last_row = -1
        for i, n in enumerate(scheduled):
            row = int(math.floor(math.log(i + 1, 2)))

            if row != last_row:
                output.write('\n')
            columns = 2 ** row
            col_width = int(math.floor(total_width / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        print(output.getvalue())
        print('-' * total_width)
        print()

    def commonaview(self, scheduled):
        nowrange = 3 if len(scheduled) >= 3 else len(scheduled)
        return [ heapq.heappop(scheduled) for _ in range(nowrange) ]

    def recommandationaview(self, scheduled, _resd):
        nowrange = 3 if len(scheduled) >= 3 else len(scheduled)
        caview = [ heapq.heappop(scheduled) for _ in range(nowrange) ]
        if (2 <= nowrange):
            for i in _resd:
                if i[1] == caview[0]:
                    # print(i[1], caview[0])
                    # 2024.9.19 i[2] = localcircuit
                    print('- Prime   : {:>16}'.format( ''.join([i[0], '.', i[2]]) ))
            for i in _resd:
                if i[1] == caview[1]:
                    # print(i[1], caview[1])
                    # 2024.9.19 i[2] = localcircuit
                    print('- Standby : {:>16}'.format( ''.join([i[0], '.', i[2]]) ))
        else:
            for i in _resd:
                if i[1] == caview[0]:
                    # print(i[1], caviw[0])
                    # 2024.9.19 i[2] = localcircuit
                    print('- Singleton : {:>16}'.format( ''.join([i[0], '.', i[2]]) ))
        return caview
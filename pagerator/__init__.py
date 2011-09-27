import math

def _iterate_over_pages(getter, page_size, start_from, upper_bound):
    page = int(math.floor(start_from / page_size))

    if upper_bound is None:
        num_items = None
    else:
        num_items = upper_bound - start_from

    if num_items != 0:
        start_from -= page * page_size

        results = getter(page)
        while results:
            for item in results:
                if start_from > 0:
                    start_from -= 1
                else:
                    yield item
                    if upper_bound is not None:
                        num_items -= 1
                        if num_items == 0:
                            return
            page += 1
            results = getter(page)


class IterableQuery(object):
    def __init__(self, getter, page_size, start_from = 0, upper_bound = None):
        self._getter = getter
        self._page_size = page_size
        self._start_from = start_from
        self._upper_bound = upper_bound

    def __iter__(self):
        return _iterate_over_pages(
            self._getter,
            self._page_size,
            self._start_from,
            self._upper_bound,
        )

    def __getitem__(self, key):
        if isinstance(key, slice):
            start = self._start_from
            if key.start is not None:
                if key.start < 0:
                    raise KeyError('Negative indexes aren\'t not supported')
                start += key.start

            if key.stop is None:
                upper_bound = self._upper_bound
            else:
                if self._upper_bound is None:
                    upper_bound = self._start_from + key.stop
                else:
                    upper_bound = min(self._upper_bound, start + key.stop)

            return IterableQuery(
                self._getter,
                self._page_size,
                start_from = start,
                upper_bound = upper_bound,
            )
        raise KeyError('Key %r unsupported.' % (key,))


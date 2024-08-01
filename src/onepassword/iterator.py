import asyncio


class SDKIterator:
    def __init__(self, obj):
        self.obj = obj
        self.index = 0
        self.lock = asyncio.Lock()

    def __aiter__(self):
        return self

    async def __anext__(self):
        async with self.lock:
            if self.index >= len(self.obj):
                raise StopAsyncIteration

            next_obj = self.obj[self.index]
            self.index += 1
            return next_obj

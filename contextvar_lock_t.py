import asyncio
from contextvars import ContextVar

# 模拟一个全局的锁仓库，确保同一个 Key 返回同一个锁对象
class LockStore:
    def __init__(self):
        self._locks = {}

    def get_lock(self, key):
        if key not in self._locks:
            self._locks[key] = asyncio.Lock()
        return self._locks[key]

lock_store = LockStore()

class LockManager:
    def __init__(self):
        # 每个协程的任务上下文中，都会存储自己当前持有的那个锁
        self._ctx_var = ContextVar("current_lock")

    async def acquire(self, key):
        # 1. 根据 Key 获取对应的锁对象
        lock = lock_store.get_lock(key)
        
        # 2. 尝试竞争这把锁
        print(f"协程 {asyncio.current_task().get_name()} 尝试获取 【{key}】 的锁...")
        await lock.acquire()
        
        # 3. 竞争成功，把这把锁存入当前协程的“口袋” (ContextVar)
        self._ctx_var.set(lock)
        print(f"协程 {asyncio.current_task().get_name()} 成功拿到 【{key}】 的锁！")

    async def release(self):
        # 从当前协程的“口袋”里取出锁，谁拿的谁还
        lock = self._ctx_var.get(None)
        if lock is not None:
            lock.release()
            print(f"协程 {asyncio.current_task().get_name()} 已释放锁。")

# 业务函数：所有人都会进入这个函数
async def business_logic(mgr, user_id):
    await mgr.acquire(user_id)
    try:
        print(f"--- 协程 {asyncio.current_task().get_name()} 正在处理 {user_id} 的业务 ---")
        await asyncio.sleep(2)  # 模拟耗时操作
    finally:
        await mgr.release()

async def main():
    mgr = LockManager()
    
    # 模拟并发场景
    tasks = [
        # 协程 A 和 C 竞争“张三”，协程 B 独自处理“李四”
        asyncio.create_task(business_logic(mgr, "张三"), name="A"),
        asyncio.create_task(business_logic(mgr, "李四"), name="B"),
        asyncio.create_task(business_logic(mgr, "张三"), name="C"),
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())

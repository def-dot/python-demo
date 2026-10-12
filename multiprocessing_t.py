from multiprocessing import Process, Manager

def worker(shared_dict, shared_list, index):
    # 修改共享字典
    shared_dict[index] = f"任务 {index} 已完成"
    # 修改共享列表
    shared_list.append(index)

if __name__ == "__main__":
    # 使用 with 语句可以确保 Manager 进程在结束后自动关闭
    with Manager() as manager:
        # 创建共享的字典和列表
        d = manager.dict()
        l = manager.list()

        processes = []
        for i in range(5):
            p = Process(target=worker, args=(d, l, i))
            p.start()
            processes.append(p)

        for p in processes:
            p.join()

        print("共享字典:", d)
        print("共享列表:", l)

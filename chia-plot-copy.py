import os, shutil, time
import platform
import ctypes

def get_free_space_mb(folder):
    """
    获取磁盘剩余空间
    :param folder: 磁盘路径 例如 D:\\
    :return: 剩余空间 单位 G
    """
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024 // 1024
    else:
        st = os.statvfs(folder)
        return st.f_bavail * st.f_frsize / 1024 // 1024


def copy_data(file_inp_list, file_tar_list, key):
    file_list_inp = []
    file_list_tar = []

    for file_tar in file_tar_list:
        for root, dirs, files in os.walk(file_tar):
            for item in files:
                if item[-5:] == '.plot':
                    file_list_tar.append([root, item])

    for file_inp in file_inp_list:
        for root, dirs, files in os.walk(file_inp):
            for idx, item in enumerate(files):
                if item[-5:] == '.plot':
                    #print(root)
                    if len(file_list_tar) > 0:
                        if item not in [item[1] for item in file_list_tar]:
                            file_list_inp.append([root, item])
                        else:
                            tar_index = [item[1] for item in file_list_tar].index(item)
                            if os.path.getsize(file_list_tar[tar_index][0] + '\\' + file_list_tar[tar_index][1]) < os.path.getsize(root + '\\' + item):
                                file_list_inp.append([root, item])
                            else:
                                print(root + '\\' + item + '\t已存在于\n' + file_list_tar[tar_index][0] + '\\' + file_list_tar[tar_index][1] + '\n')
                    else:
                        file_list_inp.append([root, item])


    if len(file_list_inp) > 0:
        print('\n待拷文件有(' + str(len(file_list_inp)) + ')个：')
        for item in file_list_inp:
            print(item[0] + '\\' + item[1])
        for file_tar in file_tar_list:
            if get_free_space_mb(file_tar) > 103:
                start = time.time()
                print('\n【' + str(key) +'】开始拷贝...\t' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n' + file_list_inp[0][0] + '\\' + file_list_inp[0][1] + '\tTo\n' + file_tar + '\\' +
                      file_list_inp[0][1])
                try:
                    shutil.move(file_list_inp[0][0] + '\\' + file_list_inp[0][1], file_tar + '\\' + file_list_inp[0][1])
                except:
                    print('拷贝出错：' + file_list_inp[0][0] + '\\' + file_list_inp[0][1])
                #time.sleep(10)
                end = time.time()
                print('拷贝结束，耗时：{:.2f}分钟...\n'.format((end - start)/60))
                return 1
            else:
                print('【' + file_tar + '】空间不足')
        print('【所有】空间均不足\n')
        for i in range(3 * 60):
            st = '.' * (i % 7) + ' ' * (6 - (i % 7))
            print('\r已存在【' + str(len(file_list_tar)) + '】个文件，等待中' + st, end='')
            time.sleep(1)
        return 0

    else:
        for i in range(3 * 60):
            st = '.' * (i % 7) + ' ' * (6 - (i % 7))
            print('\r已存在【' + str(len(file_list_tar)) + '】个文件，等待中' + st, end='')
            time.sleep(1)
        return 0


def getPath():
    path_inp = []
    path_tar = []

    if os.path.exists('SSD2HDD.txt'):
        with open('SSD2HDD.txt', 'r', encoding='utf-8') as f:
            data = f.read().split('\n')
            data = [item for item in data if len(item) > 0]
            ssd_index = data.index('SSD')
            hdd_index = data.index('HDD')
            path_inp = path_inp + data[ssd_index + 1: hdd_index]
            path_tar = path_tar + data[hdd_index + 1:]

            for inp in path_inp:
                print('默认的【监控】固态硬盘地址：' + inp)
            print()

            for tar in path_tar:
                print('默认的【存入】机械硬盘地址：' + tar)
            print()

    # print('拷贝中...' + '{:.2f}%'.format(10 / 30 * 100))
    path1 = input('请输入【监控】固态硬盘地址：')
    while (path1 != ''):
        path_inp.append(path1)
        path1 = input('请输入【监控】固态硬盘地址：')

    print()

    path2 = input('请输入【存入】机械硬盘地址：')
    while (path2 != ''):
        path_tar.append(path2)
        path2 = input('请输入【存入】机械硬盘地址：')

    print()

    copy_inp = []
    copy_tar = []

    for inp in path_inp:
        if os.path.exists(inp):
            copy_inp.append(inp)
        else:
            print('【监控】地址【不存在】：' + inp)

    for tar in path_tar:
        if os.path.exists(tar):
            copy_tar.append(tar)
        else:
            print('【存入】地址【不存在】：' + tar)

    if len(copy_tar) > 0 and len(copy_inp) > 0:
        print()
        return copy_inp, copy_tar
    else:
        return getPath()


if __name__ == '__main__':

    path_inp, path_tar = getPath()

    for inp in path_inp:
        print('【监控】地址：' + inp)
    print()

    for tar in path_tar:
        print('【存入】地址：' + tar)
    print()

    key = 1
    while key > 0:
        key += copy_data(path_inp, path_tar, key)
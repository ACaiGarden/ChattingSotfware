import hashlib
import time
if __name__ == '__main__':
    '''
    hash = hashlib.md5('python'.encode('utf-8'))
    hash.update('as123.14.12.1310086sdasdasd3242545366456'.encode('utf-8'))
    print(hash.hexdigest())S
    li = [['as', ('123.14.12.13', 10086), 'sdasdasd3242545366456'], [123, 4645, 654645], [432434, 89, 232]]
    print(li[2])
    print(li[0][1][0])
    print(li[0][0]+li[0][1][0]+str(li[0][1][1])+li[0][2])
    '''
    a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    time.sleep(10)
    b = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(b-a)


# 编译：
# 将编写的C代码编译成动态链接库的形式，具体命令：
# gcc hello.c -fPIC -shared -o libhello.so
# 其中-shared代表这是动态库，-fPIC使得位置独立（如果程序本来就是独立的话会有警告，无视即可），-o指定了输出文件，改成dll后缀一样可以用。
if __name__ == '__main__':
    import ctypes  
    lib = ctypes.cdll.LoadLibrary('./libfunc.so')    
    print(lib.func(9))
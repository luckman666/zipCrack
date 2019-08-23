# -*- encoding = 'utf-8' -*- 
import zipfile
import optparse


def extractFile(zFile,password):
    """
    解压函数
    """
    try:
        zFile.extractall(pwd=password.encode('utf-8'))
        print('[+] Password = ' + password + '\n')
        return True
    except:
        return 
def main():

    parser = optparse.OptionParser("usage：" + "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='Password dictionary')

    (options, args) = parser.parse_args()

    if(options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    try:
        passFile = open(dname, 'r', )
        with open(dname, 'r', encoding = 'utf-8') as passFile:
            for line in passFile.readlines():
                password = line.strip('\n')
                flag = extractFile(zFile, password)
                if flag:
                    print('爆破成功')
                    break
    except Exception:
        print('错误输入')
        
if __name__ == '__main__':
    main()
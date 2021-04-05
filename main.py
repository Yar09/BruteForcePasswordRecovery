import string
import itertools
import time
import zipfile


def combination():
    symbols = string.ascii_lowercase + string.ascii_uppercase
    length = 1
    while True:
        for i in itertools.product(symbols, repeat=length):
            yield "".join(i)
        length += 1


def password_recovery(f):
    step = 0
    start_time = time.time()

    file = zipfile.ZipFile(fileName)
    for s in combination():
        step += 1
        try:
            file.extractall(pwd=bytes(s, "utf-8"))
        except:
            continue
        else:
            print(f'Recovered password is "{s}" on {step} step')
            print("--- %s seconds ---" % (time.time() - start_time))
            print("Speed is ", step / (time.time() - start_time), " psw/s \n")
            print(file.printdir())


fileName = "lat2.zip"
password_recovery(fileName)

print('The End!')

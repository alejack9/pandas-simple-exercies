for i in range(1, 8):
    __import__(str(i)).exec()
    print('-------------')

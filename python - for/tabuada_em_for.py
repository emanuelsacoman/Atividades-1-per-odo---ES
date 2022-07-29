def tabuada():
    for j in range(11):
        for i in range(11):
            mult=i*j
            print("{0} X {1} = {2}".format(j,i,mult))


if __name__ == "__main__":
    tabuada()
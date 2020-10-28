def create_datafile(datafile):
    open(datafile, "w+").write("0")

def update_datafile(datafile, x):
    with open(datafile, "r") as df:
        result = int(df.readline()[0]) + x

    with open(datafile, "w+") as df:
        df.write(str(result))

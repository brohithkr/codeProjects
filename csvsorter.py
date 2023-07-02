def read_from_csv(csvfile):
    rows = []
    with open(csvfile,"r") as f:
        row = []
        curstr = ""
        for i in f.read():
            curstr+=i
            if i == ",":
                row.append(curstr[:-1] if not curstr[:-1].isnumeric() else int(curstr[:-1]))
                curstr = ""
            if i == "\n":
                row.append(curstr[:-1] if not curstr[:-1].isnumeric() else int(curstr[:-1]))
                rows.append(row)
                row = []
                curstr = ""
    return rows
    


def write_to_csv(rows,csvfile):
    final_str = ""
    for i in rows:
        rowstr = ""
        for j in i:
            rowstr += str(j) + ","
        final_str += rowstr + "\n"
    with open(csvfile,"w") as f:
        f.write(final_str)


rows = read_from_csv("csvfile.csv")
print(rows)
sortedrows = sorted(rows,key=lambda x:x[2])
print(sortedrows)

write_to_csv(sortedrows,"csvfile.csv")




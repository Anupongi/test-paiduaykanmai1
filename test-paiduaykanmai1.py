number = int(input());
codes = str(input()); #RRB

tmp = "";   #R G B
count = 0;
for code in codes:
    if tmp == code:
        count += 1;
    tmp = code;
    # print(len(codes))
    if len(codes) > number:
        print("จำนวนเกิน")
        break


print("Output : ", count + "คู่")
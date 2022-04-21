number = int(input());
codes = str(input());

tmp = "";   
count = 0;
for code in codes:
    if tmp == code:
        count += 1;
    tmp = code;

print("Output : ", count )
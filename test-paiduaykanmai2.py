banknotes = int(input()); 

result = 0;
numpay = [100, 20, 10, 5, 1];

#   100
for t in numpay:
    if banknotes >= t:
        result += int(banknotes / t)
        banknotes = banknotes % t

print("Output : ", result )
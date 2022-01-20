import re
surce = open(r"input_3", "r")
text = surce.read()
counter=0
list = re.findall("[\d]", text)
print(len(list))
list2 = []

for q in range(0, 5):
    for d in str(list[0+q]):
        list2.append(int(d));
        counter = counter + 1;
print (list2)
w = 0;
print(counter);
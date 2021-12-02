string = "sagar is sagar not sa saga sagar r s"
sub_string = "sagar"
count = 0

for i in range(0, len(string) - len(sub_string)):
    found = True
    for j in range(len(sub_string)):
        if string[i + j] != sub_string[j]:
            found = False
            break
    if found:
        count += 1

print(count)
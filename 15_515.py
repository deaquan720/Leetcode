
Test = "godding"
target = "d"

i = 0

left = i
lc = 0
right = i
rc = 0

while Test[left] != target:
    left -= 1
    lc += 1
    if left == -1:
        left = len(Test) - 1

while Test[right] != target:
    right += 1
    rc += 1
    if right == len(Test):
        right = 0


print(left, lc)
print(right, rc)

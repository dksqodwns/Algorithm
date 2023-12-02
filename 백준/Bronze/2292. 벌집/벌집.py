N = int(input())
layer = 1
end = 1
while N > end:
    end += layer * 6
    layer += 1

print(layer)

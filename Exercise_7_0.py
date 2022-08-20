#reading files

# file = open('main.py')
#
# count = 0
# for lines in file:
#     print(lines)
#     count += 1
#
# print('Line count:', count)


# file = open('main.py')
# text = file.read()
#
# count = 0
# for character in text:
#     print(character)
#     count += 1
#
# print('Character count:', count)

# look only for comments - excluding all newlines
# file = open('main.py')
#
# count = 0
# for line in file:
#     line = line.rstrip()
#     if line.startswith('#'):
#         print(line)
#         count += 1
#
# print('Line count:', count)


# # exclude all comments version 1
# file = open('main.py')
#
# count = 0
# for line in file:
#     line = line.rstrip()
#     if not line.startswith('#'):
#         print(line)
#         count += 1
#
# print('Line count:', count)

# exclude all comments version 2
file = open('main.py')

count = 0
for line in file:
    line = line.rstrip()
    if '#' in line:
        continue
    print(line)
    count += 1

print('Line count:', count)
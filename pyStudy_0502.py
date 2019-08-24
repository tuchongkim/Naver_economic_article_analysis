# class Solution(object):
#     def numUniqueEmails(self, emails):
#         """
#         :type emails: List[str]
#         :rtype: int
#         """
#         email_set = set()
#         for email in emails:
#             elements = email.split('@')
#             email_set.add(elements[0].split('+')[0].replace('.', '') + elements[1])
#         return len(email_set)



# str = "test.email+alex@leetcode.com"
# tmp = str.split("@")
# print(tmp[0])
# print(tmp[1])

# print(tmp[0].split('+')[0])
# print(tmp[0].split('+')[0])






line_max = 7
for line in range(1, line_max):
    for blank in range(line_max - line):
        print(" ",end="")
    for star in range(line*2-1):
        print("*",end="")
    print()
for line in range(line_max-2,0,-1):
    for blank in range(line_max - line):
        print(" ",end="")
    for star in range(line*2-1):
        print("*",end="")
    print()
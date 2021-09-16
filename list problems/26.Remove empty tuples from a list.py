# In this article, we will see how can we remove an empty tuple from a given list of tuples. We will find various ways, in which we can perform this task of removing tuples using various methods and ways in Python.
# Examples:

# Input : tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
#                   ('krishna', 'akbar', '45'), ('',''),()]
# Output : [('ram', '15', '8'), ('laxman', 'sita'), 
#           ('krishna', 'akbar', '45'), ('', '')]

# Input : tuples = [('','','8'), (), ('0', '00', '000'), 
#                  ('birbal', '', '45'), (''), (),  ('',''),()]
# Output : [('', '', '8'), ('0', '00', '000'), ('birbal', '', 
#           '45'), ('', '')]

l=[(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('',''),()]
lst=[]
for i in l:
    if len(i)==0:
         l.remove(i)
    # for j in i:
    #     if len(j)==0:
    #         print("---------------------------------")
    #     print(j)
print(l)
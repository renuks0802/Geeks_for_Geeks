#Python program to interchange first and last elements in a list
lst=[1,2,3,4,5,6,7,8,9]
a=lst[0]
lst[0]=lst[-1]
lst[-1]=a
print(lst)

# When does 1 + 1 not equal 2?
# Things can get weirder than this. You may have heard of (or even used) tensorflow, a Python library popularly used for deep learning. It makes extensive use of operator overloading.

import tensorflow as tf
# Create two constants, each with value 1
a = tf.constant(1)
b = tf.constant(1)
# Add them together to get...
a + b

# Understanding how Python's operators work when applied to ints, strings, and lists is no guarantee that you'll be able to immediately understand what they do when applied to a tensorflow Tensor, or a numpy ndarray, or a pandas DataFrame.

# Once you've had a little taste of DataFrames, for example, an expression like the one below starts to look appealingly intuitive:

# Get the rows with population over 1m in South America
df[(df['population'] > 10**6) & (df['continent'] == 'South America')]

# When Python programmers want to define how operators behave on their types, they do so by implementing methods with special names beginning and ending with 2 underscores such as __lt__, __setattr__, or __contains__. Generally, names that follow this double-underscore format have a special meaning to Python.

# So, for example, the expression x in [1, 2, 3] is actually calling the list method __contains__ behind-the-scenes. It's equivalent to (the much uglier) [1, 2, 3].__contains__(x).

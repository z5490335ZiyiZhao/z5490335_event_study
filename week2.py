x = '''John said: "Let's learn Python together".'''
print(x)

lenth = 56
width = 33
height = 30.5
x = lenth * width * height
print("The volume of the box is {}".format(x))

domain = "From firstname.surname@unsw.edu.au Mon Feb 19 10:10:15 2024".split('@')
_domain = domain[1].split()
Domain = _domain[0]
print(_domain)

f = 0.2 + 0.2 + 0.2
print(f)
print(f==0.

x = ' some text '.strip('some text')
print(x)

w = "What"
i = "IS"
c = "CamelCase?"

print('{} {} {}'.format(w,i.lower(),c))
print(f'{w}{i}{c}')

obj.x = 1
obj.y = 2
obj.y = obj.x
obj.x = obj.y
print(obj.x)


dic0 = {'a': 1, 'b': 2, 'c': 3}
dic1 = dic0.update({'a': 0, 'd': 4})
print (dic0[0])

dic = { ('a', 'b'): 1, 'c': 2,}
print (dic)

list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']
sol = list_a[1:7]
sol.pop(2)
sol.insert(5,"including")
sol.insert(2,"good")
sol.extend(list_b)
print(sol)


current = (21+13)
(a) = current
last = (21)
(b) = last
print(f"Current price is {a} and the last price is {b}")

f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
f_suburbs.remove("Randwick")
f_suburbs.remove("Kensington")
f_suburbs.add("Fairfield")
print(f_suburbs)

f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
f_suburbs.pop("Randwick")
f_suburbs.pop("Kensington")

f_suburbs["Fairfield"] = 18081
f_suburbs["Fairfield East"] = 5273
f_suburbs["Fairfield Heights"] = 7517
f_suburbs["Fairfield West"] = 11575
f_suburbs["Fairlight"] = 5840
f_suburbs["Fiddletown"] = 233
f_suburbs["Five Dock"] = 9356
f_suburbs["Forest Glen"] = None
f_suburbs["Forest Lodge"] = 4583
f_suburbs["Forestville"] = 8329
f_suburbs["Freemans Reach"] = 1973
f_suburbs["Freshwater"] = 8866
print(f_suburbs)

import numpy as np
import matplotlib.pyplot as plt

# Define the range of values for X and Y
x_values = np.linspace(-2, 2, 1000)
y_values = np.linspace(-2, 2, 5)

# Define the CDFs for X and Y
cdf_x = np.piecewise(x_values, [x_values < -1, (x_values >= -1) & (x_values <= 1), x_values > 1], [0, lambda x: (x + 1) / 2, 1])
cdf_y = np.piecewise(x_values, [x_values < -1, x_values == -1, x_values > -1], [0, 0.5, 1])

# Plot the CDFs
plt.plot(x_values, cdf_x, label='CDF of ˜X')
plt.plot(x_values, cdf_y, label='CDF of ˜Y')
plt.xlabel('Values')
plt.ylabel('Cumulative Probability')
plt.title('Cumulative Distribution Functions')
plt.legend()
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Define the range of values for X and Y
x_values = np.linspace(-2, 2, 1000)
y_values = [-1, 1]
y_probs = [0.5, 0.5]

# Define the PDFs for X and Y
pdf_x = np.where((x_values >= -1) & (x_values <= 1), 1/2, 0)
pdf_y = np.array([0.5 if value in y_values else 0 for value in x_values])

# Plot the PDFs in two different colors
plt.plot(x_values, pdf_x, label='PDF of ˜X', color='blue')
plt.stem(x_values, pdf_y, label='PDF of ˜Y', linefmt='orange', markerfmt='o', basefmt=' ', use_line_collection=True)
plt.xlabel('Values')
plt.ylabel('Probability Density')
plt.title('Probability Density Functions')
plt.legend()
plt.grid(True)
plt.show()


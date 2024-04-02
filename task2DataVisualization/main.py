import requests
import matplotlib.pyplot as plt

data = requests.get('http://localhost:5000/').json()

for key in data.keys():
    data[key] = sum(data[key])/len(data[key])

print(data)

plt.bar(data.keys(), data.values(), color="maroon", width=0.4)
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Average marks obtained by students")
plt.show()
plt.savefig("Average_Marks.png")

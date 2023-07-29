import matplotlib.pyplot as plt

def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

file_content = read_txt_file('Algorithm/data/test.txt')
data_list = [int(num) for num in file_content.split()]

plt.plot(data_list, marker='o', linestyle='-', color='b', label='Data Points')

# Add labels and title
plt.xlabel('X-axis (Data Points Index)')
plt.ylabel('Y-axis (Values)')
plt.title('Plot of Data Points')

# Add a legend
plt.legend()

# Show the plot
plt.show()
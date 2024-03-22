def y_func(x):
    return (30 / 8211) * x + 59.98780487804878


def calculate_y(x):
    y = y_func(x)
    return y


# 主循环，用于接收用户输入并计算y值
while True:
    x_input = input("请输入一个x值 (或输入'q'退出): ")
    if x_input.lower() == 'q':  # 忽略大小写，允许用户输入'Q'或'q'退出
        break
    try:
        x_value = float(x_input)
        y_output = y_func(x_value)
        print(f"对应的y值为: {y_output}")
    except ValueError:
        print("输入无效，请输入一个数字或'q'退出。")

    # 如果您还想绘制函数图像，可以继续使用之前的代码（这部分可以放在循环外部）
import matplotlib.pyplot as plt

# 创建x值的范围用于绘图
x_values = range(-10000, 10001, 100)
y_values = [y_func(x) for x in x_values]

# 绘制图像
plt.plot(x_values, y_values, label='y = (30 / 8211) * x + 59.98780487804878')

# 设置标题和坐标轴标签
plt.title('函数图像')
plt.xlabel('x')
plt.ylabel('y')

# 显示图例
plt.legend()

# 显示网格
plt.grid(True)

# 显示图像
plt.show()
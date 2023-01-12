import matplotlib.pyplot as plt
import numpy
from celluloid import Camera

fig = plt.figure()
axes = fig.add_subplot(projection='3d')
camera = Camera(fig)


def makeData(t):
    # Строим сетку в интервале от -10 до 10, имеющую 100 отсчетов по обоим координатам
    x = numpy.linspace(-20, 20, 100)
    y = numpy.linspace(0, 40, 100)

    # Создаем двумерную матрицу-сетку
    xgrid, ygrid = numpy.meshgrid(x, y)

    # В узлах рассчитываем значение функции
    z = 0.5 * numpy.sin(0.5 * numpy.sqrt(xgrid ** 2 + ygrid ** 2+t))
    return xgrid, ygrid, z

for i in range(10):
    t = numpy.pi * i * 0.1
    x, y, z = makeData(t)
    axes.plot_surface(x, y, z,cmap='Spectral')
    camera.snap()

animation = camera.animate()
animation.save('waves.gif')


# animation.show()

# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import numpy as np
#
# plt.style.use('dark_background')
#
# fig = plt.figure()
# ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
# line, = ax.plot([], [], lw=2)
#
#
# # Функция инициализации.
# def init():
#     # создение пустого графа.
#     line.set_data([], [])
#     return line,
#
#
# xdata, ydata = [], []
#
#
# # функция анимации
# def animate(i):
#     t = 0.1 * i
#
#     # x, y данные на графике
#     x = t * np.sin(t)
#     y = t * np.cos(t)
#
#     # добавление новых точек в список точек осей x, y
#     xdata.append(x)
#     ydata.append(y)
#     line.set_data(xdata, ydata)
#     return line,
#
#
# # Заголовок анимации
# plt.title('Создаем спираль в matplotlib')
# # Скрываем лишние данные
# plt.axis('off')
#
# # Вызов анимации.
# anim = animation.FuncAnimation(fig, animate, init_func=init,
#                                frames=500, interval=20, blit=True)
#
# # Сохраняем анимацию как gif файл
# anim.save('coil.gif', writer='imagemagick')
# anim.show()
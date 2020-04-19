import numpy as np
import matplotlib.pyplot as plt


def func(x, q, d):

    return 1 - (1 - q * x) ** d

def plot_comparisons():

    colors = ['r', 'g', 'y', 'm', 'b']
    qd = [(0.1, 2), (0.1, 5), (0.1, 10), (0.1, 15), (0.15, 15)]

    for j, (q, d) in enumerate(qd):

        values = []
        x = 1
        for i in range(20):
            v = func(x, q, d)
            values.append((x, v))
            x = v

        fun_vals = []
        for x in np.arange(0, 1, 0.02):
            fun_vals.append(func(x, q, d))

        # arrows = []
        for i in range(0, len(values) - 1):
            dx = values[i + 1][0] - values[i][0]
            dy = values[i + 1][1] - values[i][1]
            print(values[i][0], values[i][1], dx, dy)
            # arrows.append([values[0], values[1], dx, dy])
            plt.arrow(values[i][0], values[i][1], dx, dy, color=colors[j], width=0.003, head_width=0.02, length_includes_head=True)

        values = sorted(values, key=lambda x: x[0])
        label = f'q={q} d={d}'
        plt.plot([p[0] for p in values], [p[1] for p in values], c=colors[j], label=label, linewidth=1)
        plt.plot(np.arange(0, 1, 0.02), fun_vals, c=colors[j], linestyle='--')

        
        #label = f'q={q} d={d}'
        # plt.plot([p[0] for p in values], [p[1] for p in values], label=label)
        # plt.arrow([p[0] for p in arrows], [p[1] for p in arrows], [p[2] for p in arrows], [p[3] for p in arrows], label=label)

    plt.plot(np.arange(0, 1, 0.02), np.arange(0, 1, 0.02), 'k--', label='f(x)=x')

    plt.xlabel('x')
    plt.ylabel('f(x)')

    plt.legend()
    plt.show()



def plot_decrease():

    q = 0.2
    d = 10

    total_days = 120
    active_days = 15
    # gov_action = 30
    # gov_eff = 0.8
    periodic = 7

    # ae = [(15, 0.6), (15, 0.8), (30, 0.6), (30, 0.8), (45, 0.6), (45, 0.8)]
    ae = [(5, 0.95), (30, 0.95)]

    for j, (gov_action, gov_eff) in enumerate(ae):

        q = 0.2
        d = 10

        values = [(1, func(1, q, d))]
        for i in range(total_days):
            prev_x, prev_y  = values[-1]

            cur_x = func(prev_x, q, d)
            cur_y = func(cur_x, q, d)

            dx = (cur_x - prev_x) / active_days
            dy = (cur_y - prev_y) / active_days

            correct_x = prev_x + dx
            correct_y = prev_y + dy

            values.append((correct_x, correct_y))

            try:
                plt.arrow(prev_x, prev_y, dx, dy, color='b', width=0.001, head_width=0.009, length_includes_head=True)
            except:
                print(f'Unable to plot {values[i]}')

            if i > gov_action and i % periodic == 0:
                q = q * gov_eff
                d = d * gov_eff

                d = max(d, 1)
                q = max(q, 0.01)

            print(d)

    '''
    for i in range(0, len(values) - 1):
        print(values[i])
        dx = values[i + 1][0] - values[i][0]
        dy = values[i + 1][1] - values[i][1]
        print(values[i][0], values[i][1], dx, dy)
        try:
            plt.arrow(values[i][0], values[i][1], dx, dy, color='b', width=0.003, head_width=0.02, length_includes_head=True)
        except:
            print(f'Unable to plot {values[i]}')
    '''

    plt.plot(np.arange(0, 1, 0.02), np.arange(0, 1, 0.02), 'k--', label='f(x)=x')

    plt.xlabel('x')
    plt.ylabel('f(x)')

    plt.show()

if __name__ == '__main__':
    plot_decrease()
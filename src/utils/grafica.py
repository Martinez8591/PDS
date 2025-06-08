import matplotlib.pyplot as plt


def continuous_plotter(
        ind_var, dep_var,
        title: str = "", graph_label: str = "",
        x_label: str = "", y_label: str = ""):
    plt.plot(ind_var, dep_var, label=graph_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
def discrete_plotter(
        ind_var, dep_var,
        title: str = "", graph_label: str = "",
        x_label: str = "", y_label: str = ""):
    plt.stem(ind_var, dep_var, label=graph_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
def combined_plotter(
        cont_ind_var, cont_dep_var,
        disc_ind_var, disc_dep_var,
        title: str = "", graph_label: str = "",
        x_label: str = "", y_label: str = ""):

    plt.plot(cont_ind_var, cont_dep_var, label=graph_label + " (continua)", color='black')
    plt.stem(disc_ind_var, disc_dep_var, label=graph_label + " (discreta)")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

def combined_3plotter(
            cont_ind_var, cont_dep_var,
            cont_ind_var2, cont_dep_var2,
            disc_ind_var, disc_dep_var,
            title: str = "", graph_label: str = "",
            x_label: str = "", y_label: str = ""):
        plt.plot(cont_ind_var, cont_dep_var, label=graph_label + " (continua)", color='black')
        plt.plot(cont_ind_var2, cont_dep_var2, label=graph_label + " (continua de 1)", color="red")
        plt.stem(disc_ind_var, disc_dep_var, label=graph_label + " (discreta)")
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(loc='upper right')
        plt.grid(True)
        plt.show()
def continuous_step(
        ind_var, dep_var,
        title: str = "", graph_label: str = "",
        x_label: str = "", y_label: str = ""):
    plt.step(ind_var, dep_var, label=graph_label)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
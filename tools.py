import os
import shutil
import matplotlib.pyplot as plt


class PDF():
    def __init__(self, fig_folder):
        self.fig_folder = fig_folder
        self.fig_count = 0

        shutil.rmtree(fig_folder, ignore_errors=True)
        os.makedirs(fig_folder)

    def export(self, name=None):
        if name is None:
            file = f"{self.fig_folder}{self.fig_count:02d}.pdf"
        else:
            file = f"{self.fig_folder}{name}.pdf"
        plt.savefig(file, bbox_inches='tight')
        print(f"Export PDF : {file}\n")        
        self.fig_count += 1
pdf = PDF("img/1_ABC/")
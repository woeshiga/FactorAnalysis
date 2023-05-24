import numpy as np
from sklearn.decomposition import FactorAnalysis
import tkinter as tk
from tkinter import messagebox, filedialog

class FactorAnalysisApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Факторный анализ")
        self.window.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        label_samples = tk.Label(self.window, text="Количество сэмплов:")
        label_samples.pack()
        self.entry_samples = tk.Entry(self.window)
        self.entry_samples.pack()

        label_features = tk.Label(self.window, text="Количество признаков:")
        label_features.pack()
        self.entry_features = tk.Entry(self.window)
        self.entry_features.pack()

        label_max_factors = tk.Label(self.window, text="Максимальное количество факторов:")
        label_max_factors.pack()
        self.entry_max_factors = tk.Entry(self.window)
        self.entry_max_factors.pack()

        button_analyze = tk.Button(self.window, text="Выполнить факторный анализ", command=self.perform_factor_analysis)
        button_analyze.pack()

    def perform_factor_analysis(self):
        try:
            num_samples = int(self.entry_samples.get())
            num_features = int(self.entry_features.get())
            max_factors = int(self.entry_max_factors.get())

            file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
            if not file_path:
                return

            data = np.genfromtxt(file_path, delimiter=',')
            X = data[:num_samples, :num_features]

            fa = FactorAnalysis(n_components=max_factors, random_state=0)
            X_factors = fa.fit_transform(X)

            messagebox.showinfo("Результаты", f"Матрица факторных нагрузок:\n{fa.components_}\n\nМатрица факторных значений:\n{X_factors}")

        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = FactorAnalysisApp()
    app.run()

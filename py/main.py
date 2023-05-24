import numpy as np
from sklearn.decomposition import FactorAnalysis
import tkinter as tk
from tkinter import messagebox, filedialog

def perform_factor_analysis():
    try:
        # Чтение входных данных из текстовых полей
        num_samples = int(entry_samples.get())
        num_features = int(entry_features.get())
        max_factors = int(entry_max_factors.get())

        # Загрузка данных из файла
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return

        # Чтение данных из файла
        data = np.genfromtxt(file_path, delimiter=',')  # Предполагается, что файл CSV содержит только числовые данные
        X = data[:num_samples, :num_features]

        # Факторный анализ
        fa = FactorAnalysis(n_components=max_factors, random_state=0)
        X_factors = fa.fit_transform(X)

        # Вывод результатов
        messagebox.showinfo("Результаты", f"Матрица факторных нагрузок:\n{fa.components_}\n\nМатрица факторных значений:\n{X_factors}")

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")

# Создание графического интерфейса с использованием Tkinter
window = tk.Tk()
window.title("Факторный анализ")
window.geometry("500x500")

# Метка и текстовое поле для количества сэмплов
label_samples = tk.Label(window, text="Количество сэмплов:")
label_samples.pack()
entry_samples = tk.Entry(window)
entry_samples.pack()

# Метка и текстовое поле для количества признаков
label_features = tk.Label(window, text="Количество признаков:")
label_features.pack()
entry_features = tk.Entry(window)
entry_features.pack()

# Метка и текстовое поле для максимального количества факторов
label_max_factors = tk.Label(window, text="Максимальное количество факторов:")
label_max_factors.pack()
entry_max_factors = tk.Entry(window)
entry_max_factors.pack()

# Кнопка для запуска факторного анализа
button_analyze = tk.Button(window, text="Выполнить факторный анализ", command=perform_factor_analysis)
button_analyze.pack()

# Запуск главного цикла графического интерфейса
window.mainloop()

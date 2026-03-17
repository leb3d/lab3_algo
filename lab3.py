import numpy as np

def generate_data():
    return np.random.randint(-50, 91, size=(3, 4))

def process_data(matrix):
    row_min = np.argmin(matrix) // matrix.shape[1]
    row_max = np.argmax(matrix) // matrix.shape[1]

    swapped_matrix = matrix.copy()
    swapped_matrix[[row_min, row_max]] = swapped_matrix[[row_max, row_min]]

    reshaped_matrix = swapped_matrix.reshape(6, 2)
    first_three_rows = reshaped_matrix[:3]
    final_matrix = reshaped_matrix[:-1]

    return row_min, row_max, swapped_matrix, reshaped_matrix, first_three_rows, final_matrix

def print_results(matrix, row_min, row_max, swapped_matrix, reshaped_matrix, first_three_rows, final_matrix):
    print("Початкова матриця 3x4:")
    print(matrix)

    print(f"\nМінімальний елемент: {matrix.min()}")
    print(f"Максимальний елемент: {matrix.max()}")
    print(f"Рядок з мінімальним елементом: {row_min + 1}")
    print(f"Рядок з максимальним елементом: {row_max + 1}")

    print("\nМатриця після обміну рядків:")
    print(swapped_matrix)

    print("\nМатриця після зміни розмірності на 6x2:")
    print(reshaped_matrix)

    print("\nПерші три рядки масиву 6x2:")
    print(first_three_rows)

    print("\nМасив після вилучення останнього рядка:")
    print(final_matrix)

def main():
    matrix = generate_data()
    row_min, row_max, swapped_matrix, reshaped_matrix, first_three_rows, final_matrix = process_data(matrix)
    print_results(matrix, row_min, row_max, swapped_matrix, reshaped_matrix, first_three_rows, final_matrix)

if __name__ == "__main__":
    main()

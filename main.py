from src.utils import load_data, sorted_data, list_transaction
from config import FILE_PATH


def main():
    data_json = load_data(FILE_PATH)
    json_sorted = sorted_data(data_json)
    transactions = list_transaction(json_sorted)
    print('\n'.join(transactions[:5]))


if __name__ == "__main__":
    main()

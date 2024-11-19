from pathlib import Path

data_path = Path("./data")  # Define the path to the data directory

def search(search_query):
    # Define every file path for files in data_path into an array
    data_file_paths = [str(file) for file in data_path.iterdir() if file.is_file()]

    # Read the content of all files into a list
    data = [Path(file).read_text() for file in data_file_paths]

    # Iterate through data with enumerate for index and row
    for index, row in enumerate(data):
        print(data)
        if search_query in row:
            words = row.lower().split()
            words_match_query = words.count(search_query)  # Count matches directly
            print(words_match_query, "matches found in file", data_file_paths[index])

# Get search query from user input
search_query = input("Search: ").lower()
search(search_query)
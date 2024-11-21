from pathlib import Path

data_path = Path("./data")  # Define the path to the data directory

# Define every file path for files in data_path into an arpray
data_file_paths = [str(file) for file in data_path.iterdir() if file.is_file()]

# Read the content of all files into a list
data = [Path(file).read_text(encoding="utf-8") for file in data_file_paths]

def search(search_query):

    found_any = False  # Track if any matches were found
    for index, file in enumerate(data):
        if search_query in file.lower():
            found_any = True # Set to True if any matches were found
            words = file.lower().split()
            words_match_query = words.count(search_query)  # Count matches directly
            if words_match_query > 0:
                print(words_match_query, "matches found in file", data_file_paths[index])
            
    if found_any:
        user_input = input("Want to show location of words in files? (Y/n)")
        if user_input.lower() == "y":
            show_location(search_query)
        return
    else: 
        print("No results found for:", search_query)
        
def show_location(search_query):
    for index, file in enumerate(data):  # Iterate over files with their indices
        if search_query in file:
            lines = file.splitlines()  # Split file content into lines
            for line_num, line in enumerate(lines, start=1):  # Enumerate lines starting at 1
                words = line.lower().split()
                words_match_query = words.count(search_query)
                if words_match_query > 0:
                    print(f"For file: {data_file_paths[index]}, '{search_query}' found in Ln {line_num}")
    
while True:
    # Get search query from user input
    search_query = input("Search: ").lower()
    
    if search_query == "/exit":
        print("Goodbye!..")
        break
    
    search(search_query)
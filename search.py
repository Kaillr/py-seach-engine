from pathlib import Path
import os

# Define the data directory path
data_path = Path("./data")

# Define every file path for files in data_path into an array
data_file_paths = [file for file in data_path.iterdir() if file.is_file()]

# Read the content of all files into a list
data = [Path(file).read_text(encoding="utf-8") for file in data_file_paths]

def search(search_query):
    found_any = False # Track if any matches were found
    for index, file in enumerate(data): # Track the index and value in data
        if search_query in file.lower():
            found_any = True # Set to True if any matches were found
            words = file.lower().split()
            words_match_query = words.count(search_query) # Count matches directly
            if words_match_query > 0:
                print(words_match_query, "matches found in file", data_file_paths[index])
            
    if found_any:
        user_input = input("Want to show location of words in files? (Y/n): ")
        if user_input.lower() == "y":
            show_location(search_query)
        return
    else: 
        print("No results found for:", search_query)
        
def show_location(search_query): # Function to show location of words in files
    for index, file in enumerate(data): # Track the index and value in data
        if search_query in file:
            lines = file.splitlines() # Split file content into lines
            for line_num, line in enumerate(lines, start=1): # Enumerate lines starting at 1
                words = line.lower().split()
                words_match_query = words.count(search_query) # Count how many words match search query in line
                if words_match_query > 0:
                    print(f"For file: {data_file_paths[index].name}, '{search_query}' found in Ln {line_num}") # prints the file and line where the search query is found
    enter_to_continue()


def clear(): # Clear console function
    os.system( # Executes a terminal command
              "cls" if os.name == "nt" # Use "cls" to clear the terminal on Windows
              else "clear") # Use "clear" to clear the terminal on Unix-based systems


def enter_to_continue(): # Pres enter to continue function
    input("Press Enter to continue to search...")


while True:
    clear() # Clear console before each search iteration
    
    print("""
 ____________________________________________
 
|                Command List                |
 ____________________________________________
 
| Available commands:                        |
|  /list - Lists the files in data directory |
|  /read (filename) - Reads content of file  |
|  /exit - Exit the program                  |
 ____________________________________________ 
          """)
    search_query = input("Search: ").lower() # Get search query from user input
    
    
    if search_query.startswith("/"): # if search query starts with "/"
        if search_query == "/exit":
            print("Goodbye!..")
            break
        elif search_query == "/list":
            for file in data_file_paths:
                print(file.name)
            enter_to_continue()
        elif search_query.startswith("/read"):
            found_file = False
            for index, file in enumerate(data_file_paths):
                query_file_name = search_query.split(" ", 1)[1]
                if query_file_name == data_file_paths[index].name:
                    found_file = True
                    print(data_file_paths[index].read_text(encoding="utf-8"))
                    enter_to_continue()
            if not found_file:
                input("File not found.")
        else:
            print("Invalid command.")
            enter_to_continue()

    
    if len(search_query) > 0 and not search_query.startswith("/"): # Check if search query contains at least one character
        search(search_query)
    else:
        print("Please enter a valid search query.") # Prints error if search query is empty
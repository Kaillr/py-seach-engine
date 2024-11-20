
# Python Search Engine

**Python Search Engine** is a simple Python-based utility that allows you to search for a keyword within a directory of text files. It reads all files from a specified `data` folder and identifies how many times the keyword appears in each file. Results show the number of matches and the corresponding file.



## Prerequisites

Make sure you have the following installed:

- **`pyenv`**: A tool for managing multiple Python versions.

### Installing `pyenv`
Follow the instructions on the [pyenv installation page](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation) to install `pyenv`.  
To integrate `pyenv` with your shell, follow the instructions [here](https://github.com/nvm-sh/nvm#deeper-shell-integration).

## Installing Local Python Version

1. Install the Python version specified in the `.python-version` file:
   ```bash
   pyenv install
   ```
2. Set the local Python version:
   ```bash
   pyenv local
   ```

## Initialize Virtual Environment (`venv`)

1. In the project's root directory, create a virtual environment:
   ```bash
   python -m venv .venv
   ```

## Activating the Virtual Environment

Activate the virtual environment by running the appropriate command based on your operating system and shell:
    
<table>
  <thead>
    <tr>
      <th>Platform</th>
      <th>Shell</th>
      <th>Command to activate virtual environment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">POSIX</td>
      <td>bash/zsh</td>
      <td><code>$ source .venv/bin/activate</code></td>
    </tr>
    <tr>
      <td>fish</td>
      <td><code>$ source .venv/bin/activate.fish</code></td>
    </tr>
    <tr>
      <td>csh/tcsh</td>
      <td><code>$ source .venv/bin/activate.csh</code></td>
    </tr>
    <tr>
      <td>pwsh</td>
      <td><code>$ .venv/bin/Activate.ps1</code></td>
    </tr>
    <tr>
      <td rowspan="2">Windows</td>
      <td>cmd.exe</td>
      <td><code>C:\&gt; .venv\Scripts\activate.bat</code></td>
    </tr>
    <tr>
      <td>PowerShell</td>
      <td><code>PS C:\&gt; .venv\Scripts\Activate.ps1</code></td>
    </tr>
  </tbody>
</table>

To deactivate the virtual environment, simply run:
```bash
deactivate
```

## Install Local Python Packages

1. Make sure the virtual environment is activated.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Search Engine

1. Ensure the virtual environment is activated.
2. Run the search engine script:
   ```bash
   python search.py
   ```

## Additional Resources
- For more details on **`pyenv`**, visit the [pyenv documentation](https://github.com/pyenv/pyenv#readme).
- For more details on **`venv`**, visit the [venv documentation](https://docs.python.org/3/library/venv.html).

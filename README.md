# Second_CI_Pipeline

A Python project demonstrating **Continuous Integration (CI)** with a **GitHub branch workflow** using GitHub Actions, Python, and pytest. Each of the 10 Python programs lives on its own feature branch and is tested automatically by GitHub Actions before being merged into `main`.

---

## Project Overview

The project covers the following Python programming problems:

- Checking whether a string is a pangram
- Counting the words in a sentence
- Finding the first non-repeating character in a string
- Checking whether a list is sorted
- Moving all zeros to the end of a list
- Finding the most frequent element in a list
- Rotating a string by K positions
- Finding the missing number using XOR
- Transposing a matrix
- Finding the Greatest Common Divisor (GCD)

---

## Technologies Used

- **Python 3** — implementing the programs
- **pytest** — automated testing
- **Git and GitHub** — version control, branching, and pull requests
- **GitHub Actions** — automated testing through CI

---

## Project Structure

```
Second_CI_Pipeline/
├── .github/
│   └── workflows/
│       └── ci.yml
├── Codes/
│   ├── __init__.py
│   ├── pangram.py
│   ├── count_words.py
│   ├── first_non_repeating.py
│   ├── check_sorted.py
│   ├── move_zeros.py
│   ├── most_frequent.py
│   ├── rotate_string.py
│   ├── missing_number_xor.py
│   ├── transpose_matrix.py
│   └── gcd.py
├── Test_Cases/
│   ├── __init__.py
│   ├── test_pangram.py
│   ├── test_count_words.py
│   ├── test_first_non_repeating.py
│   ├── test_check_sorted.py
│   ├── test_move_zeros.py
│   ├── test_most_frequent.py
│   ├── test_rotate_string.py
│   ├── test_missing_number_xor.py
│   ├── test_transpose_matrix.py
│   └── test_gcd.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Setup and Installation

1. **Get the project.** Open the repository on GitHub, click the green **Code** button, and clone it with GitHub Desktop or VS Code, or download it as a ZIP file.
2. **Open the folder in VS Code.** Open the `Second_CI_Pipeline` folder.
3. **Create a virtual environment (optional).** Create a `.venv` virtual environment using the Python extension in VS Code and select it as the interpreter.
4. **Install dependencies.** Install the packages listed in `requirements.txt`. This project only needs **pytest**.

---

## Programs

| Program                                | Program File               |
|----------------------------------------|----------------------------|
| Check Pangram String                   | `pangram.py`               |
| Count Words in a Sentence              | `count_words.py`           |
| Find the First Non-Repeating Character | `first_non_repeating.py`   |
| Check Whether a List Is Sorted         | `check_sorted.py`          |
| Move All Zeros to the End              | `move_zeros.py`            |
| Find the Most Frequent Element         | `most_frequent.py`         |
| Rotate a String by K Positions         | `rotate_string.py`         |
| Find the Missing Number Using XOR      | `missing_number_xor.py`    |
| Transpose a Matrix                     | `transpose_matrix.py`      |
| Find the Greatest Common Divisor       | `gcd.py`                   |

---

## Test Cases

Each program has its own pytest file inside the `Test_Cases` folder. The tests can be run for a single file or for the whole project using pytest in the VS Code terminal or the VS Code Testing panel.

| Test Case             | Test File                     |
|-----------------------|-------------------------------|
| Pangram               | `test_pangram.py`             |
| Count Words           | `test_count_words.py`         |
| First Non-Repeating   | `test_first_non_repeating.py` |
| Check Sorted          | `test_check_sorted.py`        |
| Move Zeros            | `test_move_zeros.py`          |
| Most Frequent Element | `test_most_frequent.py`       |
| Rotate String         | `test_rotate_string.py`       |
| Missing Number (XOR)  | `test_missing_number_xor.py`  |
| Transpose Matrix      | `test_transpose_matrix.py`    |
| GCD                   | `test_gcd.py`                 |

---

## GitHub Branch Workflow

The programs are **never committed directly to `main`**. Each program follows the same flow:

1. Start from an updated `main` branch.
2. Create a new feature branch for the program.
3. Add the program file and its test file to the branch.
4. Commit the changes with a clear message.
5. Push the branch to GitHub.
6. Open a Pull Request into `main` and wait for the GitHub Actions check to turn green.
7. Merge the Pull Request, then update the local `main` branch before starting the next program.

### Branches

| Program                | Branch Name           |
|------------------------|-----------------------|
| Pangram                | `pangram`             |
| Count Words            | `count-words`         |
| First Non-Repeating    | `first-non-repeating` |
| Check Sorted           | `check-sorted`        |
| Move Zeros             | `move-zeros`          |
| Most Frequent Element  | `most-frequent`       |
| Rotate String          | `rotate-string`       |
| Missing Number (XOR)   | `missing-number-xor`  |
| Transpose Matrix       | `transpose-matrix`    |
| GCD                    | `gcd`                 |

---

## Continuous Integration with GitHub Actions

The workflow file `.github/workflows/ci.yml` (named **Python CI**) runs automatically whenever a pull request targeting `main` is opened, updated, reopened, or marked ready for review.

The CI workflow:

1. Checks out the pull request code.
2. Sets up Python 3.12.
3. Installs the required dependencies.
4. Checks the Python syntax of all files.
5. Verifies that test files exist.
6. Runs pytest.
7. Reports whether the tests passed or failed.

To check the result, open your GitHub repository and select the **Actions** tab, or look at the checks section of the pull request. A green check indicates that the workflow completed successfully, and a red cross indicates a failure.

---

## Verification Checklist

- `main` contains `__init__.py`, `requirements.txt`, and `.github/workflows/ci.yml`.
- 10 feature branches exist on GitHub, one for each program.
- Each branch contains its program file and its test file.
- GitHub Actions shows a green check for every branch.
- All 10 pull requests are merged into `main`.
- All tests pass when pytest is run on the final `main` branch.

---

## Learning Objectives

- Practice Python problem-solving and functions.
- Write automated tests using pytest.
- Organize code and test files into separate folders.
- Use Git and GitHub branches and pull requests for version control.
- Understand how a CI pipeline automatically checks code changes before they are merged.

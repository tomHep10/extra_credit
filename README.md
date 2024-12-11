# Transactional Key-Value Store

## Overview
This project implements a transactional in-memory key-value store with the following features:

- **`begin_transaction()`**: Starts a new transaction.
- **`put(key, value)`**: Adds or updates a key-value pair during a transaction.
- **`get(key)`**: Retrieves the value of a key (only shows committed changes).
- **`commit()`**: Applies all changes made during the current transaction.
- **`rollback()`**: Reverts all changes made during the current transaction.


## Prerequisites
- **Python 3.8 or higher**

## How to Run the Code

### Clone the Repository
Run the following commands to clone the repository and navigate to the project directory and run the tests:
```bash
git clone <repository_url>
cd <repository_folder>
python3 test.py
```

Expected Output
```bash
None
No transaction in progress
None
None
6
```

## How this can Become a Real Assignment in the Future
Overall I think this assignment is good. I would say the main thing I would like to see is some improvements
when it comes to testing. For example maybe we can implement automated testing ourselves into this, or the graders
can use automated testing for it to make it easier to grade, or some unit tests you would require us to use or make ourselves.

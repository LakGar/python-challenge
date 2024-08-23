# Financial and Election Data Analysis

## Overview

This project performs analysis on two different datasets:

1. **Financial Data Analysis**: Analyzes the financial performance over a given period, calculating metrics such as total profit/loss, average changes, and identifying the greatest increase and decrease in profits.

2. **Election Data Analysis**: Analyzes election results, counting the total votes cast, calculating the percentage of votes each candidate received, and determining the winner of the election.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
2. Set up the Environment:
Ensure that Python 3.12+ is installed. You can set up a virtual environment and install the necessary packages:

    ```bash
    Copy code
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    pip install -r requirements.txt
3. Dependencies:

- pandas: For data manipulation and analysis.
- csv: For reading CSV files.
Install them via:

    ```bash
    Copy code
    pip install pandas
## Usage
### Financial Data Analysis
1. Place the financial dataset budget_data.csv in the Resources directory.
2. Run the analysis script:
    ```bash
    Copy code
    python main.py
3. The results will be printed to the terminal and exported to financial_analysis.txt.
## Election Data Analysis
1. Place the election dataset election_data.csv in the Resources directory.
2. Run the election analysis script:
    ```bash
    Copy code
    python main.py
3. The results will be printed to the terminal and exported to election_results.txt.
## Files
- main.py: The main script to run both financial and election data analyses.
- Resources/: Contains the datasets used in the analysis.
  - budget_data.csv
  - election_data.csv
- financial_analysis.txt: The output file for the financial analysis.
- election_results.txt: The output file for the election analysis.
## Results
### Financial Analysis
The script calculates the following:

- Total number of months.
- Net total amount of "Profit/Losses" over the entire period.
- Average change in "Profit/Losses" over the period.
- Greatest increase in profits (date and amount).
- Greatest decrease in profits (date and amount).
### Election Analysis
The script provides: 
- Total votes cast.
- Percentage and total votes for each candidate.
- The winner of the election.
## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

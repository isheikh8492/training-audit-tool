# Training Audit Tool

## Description

The **Training Audit Tool** is a console-based Python application designed to process training data from a `.json` file and generate useful reports. The tool reads training data from a file (`trainings.txt`) and outputs three different reports in JSON format:

1. **Task 1**: A report listing each completed training along with the count of how many people have completed it.
2. **Task 2**: A report of users who completed specified trainings in a given fiscal year.
3. **Task 3**: A report listing all people who have completed trainings that are either expired or will expire soon (within one month).

## Project Structure

- **data/**
  - `trainings.txt`: Input JSON file containing training data.
  
- **output/**
  - `output_task_1.json`: Generated output JSON file for Task 1.
  - `output_task_2.json`: Generated output JSON file for Task 2.
  - `output_task_3.json`: Generated output JSON file for Task 3.

- **tasks/**
  - `task1.py`: Code for Task 1 - counting completed trainings.
  - `task2.py`: Code for Task 2 - listing users trained in a specific fiscal year.
  - `task3.py`: Code for Task 3 - finding expired or soon-to-expire trainings.

- **venv/** (optional): Virtual environment directory for managing project dependencies.

- `data_loader.py`: Code for loading the input data.
- `main.py`: Main script to run all the tasks and generate the reports.
- `requirements.txt`: List of required Python packages.
- `README.md`: Documentation for the project.

## Requirements

To run this project, you need:

- Python 3.x
- Required Python packages listed in `requirements.txt`

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/isheikh8492/training-audit-tool.git
   cd training-audit-tool
   ```

2. **Set Up a Virtual Environment** (Optional):

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - On **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```

3. **Install Required Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. **Ensure Input Data File Exists**:

   Ensure the `data/trainings.txt` file exists with the appropriate training data in JSON format.

2. **Run the Main Script**:

   Execute the main script to generate the reports:

   ```bash
   python main.py
   ```

3. **Generated Reports**:

   The generated reports will be saved as JSON files in the `output/` directory:
   - `output_task_1.json`: Count of completed trainings.
   - `output_task_2.json`: Users who completed specified trainings in the fiscal year 2024.
   - `output_task_3.json`: Users with expired or expiring trainings as of the given reference date.

## Function Descriptions

- **Task 1** (`task1.py`): Counts completed trainings for each training type and generates `output_task_1.json`.
- **Task 2** (`task2.py`): Lists users who completed specified trainings in a given fiscal year and generates `output_task_2.json`.
- **Task 3** (`task3.py`): Finds users with expired or soon-to-expire trainings and generates `output_task_3.json`.

## Example Output

Below are examples of what each output file might look like:

- **`output_task_1.json`**:

  ```json
  {
      "Electrical Safety for Labs": 5,
      "X-Ray Safety": 7,
      "Laboratory Safety Training": 3
  }
  ```

- **`output_task_2.json`**:

  ```json
  {
      "Electrical Safety for Labs": ["User A", "User B"],
      "X-Ray Safety": ["User C", "User D"],
      "Laboratory Safety Training": ["User E"]
  }
  ```

- **`output_task_3.json`**:

  ```json
  {
      "User A": [
          {
              "name": "Electrical Safety for Labs",
              "status": "Expired"
          }
      ],
      "User B": [
          {
              "name": "Laboratory Safety Training",
              "status": "Expiring Soon"
          }
      ]
  }
  ```

## Troubleshooting

- **FileNotFoundError**: Ensure that the `data/trainings.txt` file is in the correct location (`data/` directory).
- **Output Directory Missing**: If the `output/` directory does not exist, the script will automatically create it before generating the reports.
- **Dependencies Not Installed**: Make sure all dependencies are installed by running `pip install -r requirements.txt`.

## Contribution

Feel free to fork the repository, open issues, or submit pull requests. Any improvements or suggestions are welcome.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For questions or support, please contact imaduddin.sheikh92@gmail.com.
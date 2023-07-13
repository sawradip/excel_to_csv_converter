
# Excel to CSV Converter: Your ultimate solution to batch Excel-to-CSV conversion!

Are you tired of manually converting a large number of Excel files to CSV format? Do you wish there was an efficient, automated way to get this mundane task done? Then **Excel to CSV Converter** is exactly what you need! This Python script automates the conversion process and liberates you from manual conversion.

With just a few lines of code, you can convert all Excel files in a directory to the universally accepted CSV format. Whether you have 10 or 1,000 Excel files, this script is here to make your life easier!

## Why You Might Need This Project

Data comes in many formats, and Excel is one of the most popular. However, Excel is not always the best format for data processing. Converting Excel to CSV can make your data easier to import into other programs, save storage space, and improve processing speed. But doing this conversion manually can be a hassle, especially when dealing with large numbers of files. This is where **Excel to CSV Converter** comes in!

## Prerequisites

- Python 3.8 or later
- LibreOffice installed and command line accessible

This script was developed on a Unix-based system (macOS/Linux). Although it should theoretically work on Windows, this has not been extensively tested.

## Installation

You can start using this tool in just a few steps:

1. Clone this repository using git:

```bash
git clone https://github.com/sawradip/excel_to_csv_converter.git
cd excel_to_csv_converter
```

2. Modify the `src_folder` and `destination_folder` variables at the end of the `src/excel_to_csv_converter.py` script to specify the directories you're working with.

## Usage

To start converting your Excel files to CSV, simply run:

```bash
python src/excel_to_csv_converter.py
```

And that's it! Your CSV files will be ready in no time!

## Future Updates

This is an ongoing project, and we have big plans for the future! Here are a few things on the horizon:

- Adding support for command line arguments to specify source and destination folders.
- Enhancing Windows compatibility and testing.
- Implementing detailed progress reporting.
- Including an option for recursive directory scanning.

## Contribution

Your suggestions and contributions are always welcome! Feel free to report issues or propose enhancements through pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

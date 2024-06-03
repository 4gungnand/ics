# Web Scraping to iCalendar

This Python script scrapes data from an HTML table and converts it into an iCalendar (.ics) file. 

## How it works

1. Reads HTML content from a .txt file.
2. Parses the HTML content using BeautifulSoup.
3. Identifies and selects a specific table from the parsed HTML.
4. Extracts headers from the table (optional, not used in ICS).
5. Extracts rows from the table.
6. Creates an iCalendar file from the extracted data.
7. Saves the iCalendar to an .ics file.

## Requirements

- Python 3
- BeautifulSoup
- ics

## Usage

1. Ensure that your HTML content is in a file named 'table_data.txt'.
2. Run the script with `python scrape.py`.
3. The script will create an .ics file named 'schedule.ics'.

## Note

This script assumes that the table you want to scrape is the second table in the HTML content (index 1). If you want to target a different table, change the index in the line `target_table = tables[1]`.
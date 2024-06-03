from bs4 import BeautifulSoup
from ics import Calendar, Event
import datetime

# Step 1: Read HTML content from txt file
with open('table_data.txt', 'r') as f:
    html_content = f.read() 

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Identify and select the specific table
# Example: Selecting the first table
tables = soup.find_all('table', {'class': 'table table-striped table-bordered table-hover'})

# Assuming you want the first table (index 0)
target_table = tables[1]  # Change the index if needed to target another table

# Step 4: Extract headers (optional, not used in ICS)
headers = [header.text.strip() for header in target_table.find_all('th')]

# Step 5: Extract rows
rows = []
for row in target_table.find('tbody').find_all('tr'):
    columns = row.find_all('td')
    row_data = [col.text.strip() for col in columns]
    rows.append(row_data)

# Step 6: Create an iCalendar file
calendar = Calendar()

for row in rows:
    no, code, subject, sks, class_, date, time, room, seat_no = row

    if not date:
        continue
    
    print(no, code, subject, sks, class_, date, time, room, seat_no)

    # Parse date and time
    start_time_str, end_time_str = time.split('-')
    start_datetime = datetime.strptime(date + ' ' + start_time_str, '%B %d, %Y %H:%M')
    end_datetime = datetime.strptime(date + ' ' + end_time_str, '%B %d, %Y %H:%M')

    # Create an event
    event = Event()
    event.name = subject
    event.begin = start_datetime
    event.end = end_datetime
    event.location = room
    event.description = f"Class: {class_}, Code: {code}, SKS: {sks}, Seat No: {seat_no}"

    # Add the event to the calendar
    calendar.events.add(event)

# Step 7: Save the calendar to an ICS file
with open('schedule.ics', 'w') as f:
    f.writelines(calendar)

print("ICS file has been created successfully.")
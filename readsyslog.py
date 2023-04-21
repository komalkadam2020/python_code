import re
from datetime import datetime

# Open the syslog file
with open('/home/ee212092/Python_WS/syslog.txt', 'r') as f:
    syslog = f.readlines()

# Define a regular expression to match the log level and message
pattern = r'(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\[(\d+)\]:\s+(.*)'

# Create a dictionary to store the syslog messages by log level
log_levels = {
    'error': [],
    'warning': [],
    'info': []
}

# Loop through each line in the syslog file
for line in syslog:
    # Match the log level and message using the regular expression
    match = re.match(pattern, line)
    if match:
        # Extract the date, log level, and message from the match
        date_str, level, pid, message = match.groups()

        # Convert the date string to a datetime object
        date = datetime.strptime(date_str, '%b %d %H:%M:%S')

        # Add the message to the appropriate list in the log_levels dictionary
        if level == 'error':
            log_levels['error'].append((date, message))
        elif level == 'warning':
            log_levels['warning'].append((date, message))
        elif level == 'info':
            log_levels['info'].append((date, message))

# Sort the messages by date
for level in log_levels:
    log_levels[level].sort(key=lambda x: x[0])

# Print the sorted messages
for level in log_levels:
    print(f'{level.upper()} MESSAGES:')
    for message in log_levels[level]:
        print(f'{message[0].strftime("%b %d %H:%M:%S")} - {message[1]}')
    print()

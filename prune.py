import os
import datetime
import re
import argparse

def select_backups(directory, extensions):
    today = datetime.date.today()
    three_months_ago = today - datetime.timedelta(days=3 * 30)  # Assuming 30 days per month for simplicity
    
    for filename in os.listdir(directory):
        if any(filename.endswith(ext) for ext in extensions):
            # Extract date from filename using regular expression
            match = re.search(r'\d{4}-\d{2}-\d{2}', filename)

            if not match:
                print(f'Unable to read date from {filename}.')
                continue

            backup_date_str = match.group()
            backup_date = datetime.datetime.strptime(backup_date_str, '%Y-%m-%d').date()
            
            if backup_date > three_months_ago:
                continue

            # Keep a backup per week for fun
            if backup_date.day % 7 == 0:
                print(f"Kept backup: {filename}")
                continue  # Skip deletion
            else:
                os.remove(os.path.join(directory, filename))
                print(f"Deleted backup: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Select and manage backup files.")
    parser.add_argument('directory', type=str, help='Directory containing backup files.')
    parser.add_argument('extensions', type=str, nargs='+', help='List of file extensions to consider (e.g. .tar.gz .zip).')

    args = parser.parse_args()

    select_backups(args.directory, args.extensions)

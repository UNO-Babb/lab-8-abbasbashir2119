#ProcessData.py
#Name: Abbas Bashir
#Date: 2025-04-10
#Assignment: Lab8 - CIST 1600

import os

def main():
    try:
        # Open the files we will be using
        inFile = open("names.dat", 'r')
        outFile = open("StudentList.csv", 'w')

        # Define mapping for year abbreviations
        year_map = {
            "Freshman": "FR",
            "Sophomore": "SO",
            "Junior": "JR",
            "Senior": "SR"
        }

        for line in inFile:
            if line.strip() == "":
                continue  # skip empty lines

            fields = line.strip().split()
            if len(fields) < 7:
                continue  # skip bad lines

            first_name = fields[0]
            last_name = fields[1]
            email = fields[2]
            student_id = fields[3]
            dob = fields[4]
            year = fields[5]
            major = " ".join(fields[6:])

            # UserID = first initial + last name + last 3 digits of ID
            first_initial = first_name[0].lower()
            last_name_clean = last_name.lower()
            if len(last_name_clean) < 5:
                last_name_clean += 'x'
            last_three_id = student_id[-3:]
            user_id = first_initial + last_name_clean + last_three_id

            # Major-Year = first 3 letters of major + year abbreviation
            major_abbr = major[:3].capitalize()
            year_abbr = year_map.get(year, year[:2].upper())  # fallback just in case
            major_year = f"{major_abbr}-{year_abbr}"

            # Write to output CSV file
            outFile.write(f"{last_name},{first_name},{user_id},{major_year}\n")

        inFile.close()
        outFile.close()

    except FileNotFoundError:
        print("Error: 'names.dat' not found. Please make sure the file is in the same directory as this script.")

if __name__ == '__main__':
    main()

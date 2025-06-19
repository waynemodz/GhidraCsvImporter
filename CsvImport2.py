#@author Wayne M (Toxic Tuning)
#@category Labeling
#@keybinding
#@menupath  CSV Import.Import Labels With Functions
#@toolbar 

import csv

csv_file = askFile("Select CSV with labels", "Import")

with open(csv_file.absolutePath, 'r') as f:
    reader = csv.DictReader(f)
    count = 0

    for row in reader:
        try:
            name = row['Name']
            addr_str = row['Address']

            if addr_str.lower().startswith("0x"):
                addr = toAddr(int(addr_str, 16))
            else:
                addr = toAddr(int(addr_str))

            if not getFunctionAt(addr):
                createFunction(addr, name)

            createLabel(addr, name, True)
            count += 1

        except Exception as e:
            print("Failed for label {}: {}".format(row.get('Name', 'N/A'), str(e)))

print("Imported {} labels.".format(count))

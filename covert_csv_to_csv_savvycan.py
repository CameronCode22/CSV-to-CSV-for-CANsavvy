import pandas as pd

#load the CSV file
df = pd.read_csv('File2_RAW.csv')

#open a new log file to write the output
with open('converted_log_2.csv', 'w') as log_file:
    #write the header
    log_file.write("Time Stamp,ID,Extended,Bus,LEN,D1,D2,D3,D4,D5,D6,D7,D8\n")

    # Loop through each row using itertuples()
    for row in df.itertuples():
        try:
            # Ensure the timestamp is cleanly handled by converting it to an integer
            time_stamp = str(row.timestamp).replace(".", "").zfill(10)  # Handle potential float conversion
            adress_id = row.canid
            extended = 'false'
            bus = row.physical_interface
            length = row.dlc

            d1 = row.byte0
            d2 = row.byte1
            d3 = row.byte2
            d4 = row.byte3
            d5 = row.byte4
            d6 = row.byte5
            d7 = row.byte6
            d8 = row.byte7

            log_file.write(f"{time_stamp},{adress_id},{extended},{bus},{length},{d1},{d2},{d3},{d4},{d5},{d6},{d7},{d8}\n")
            
        except Exception as e:
            print(f"Error processing row: {e}")

        

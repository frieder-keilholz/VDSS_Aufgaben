import csv
import json

input_path = "C:\\Users\\kjoer\\OneDrive\\Desktop\\Löschen\\VDSS\\input_text.txt"
output_path = "C:\\Users\\kjoer\\OneDrive\\Desktop\\Löschen\\VDSS\\output_data.csv"

# Converts the input text to a parseable json object
def convert_text_to_json():

    text = open(input_path, 'r')
    text_lines = text.readlines()

    for line in text_lines:
        line.strip()
        print("ok")
        convert_json_to_csv(line)

    

#converts the json object to a csv
def convert_json_to_csv(json_input):
     json_data = json.loads(json_input)
     with open(output_path, mode="a") as output_file:
         output_writer = csv.writer(output_file, delimiter=";")
         line = []
         line.clear()
         for second_level_key in json_data["localhost:27017"]:
             value = json_data["localhost:27017"][second_level_key]
             line.append(value)
         
         print(line)
         output_writer.writerow(line)

# Starts the conversion
convert_text_to_json()
        



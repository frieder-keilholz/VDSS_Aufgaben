import csv
import json

input_path = "C:\\Users\\kjoer\\OneDrive\\Desktop\\Löschen\\VDSS\\input_text.txt"
output_path = "C:\\Users\\kjoer\\OneDrive\\Desktop\\Löschen\\VDSS\\output_data.csv"

def convert_text_to_json():

    text = open(input_path, 'r')
    text_lines = text.readlines()

    for line in text_lines:
        line.strip()
        convert_json_to_csv(line)

    


def convert_json_to_csv(json_input):
     json_data = json.loads(json_input)

     with open(output_path, mode="w") as output_file:
         output_writer = csv.writer(output_file, delimiter=";")

         line.clear()
         for second_level_key in json_data["localhost:27017"][0]:
             value = json_data["localhost:27017"][0][second_level_key]
             line.appen(value)

         output_writer.writerow(line)


convert_text_to_json()
        



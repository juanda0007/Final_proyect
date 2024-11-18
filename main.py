import json
from functions import report_generator
from file_operation import get_file_content

def save_report(report, output_path):
    """
    Guarda el reporte de las palabras encontradas en un archivo JSON.
    """
    with open(output_path, 'w') as file:
        json.dump(report, file, indent=4)


def main(input_path, output_path):
    soup, words = get_file_content(input_path)
    report = report_generator(soup, words)
    save_report(report, output_path)

input_file = 'input.txt'
output_file = 'report.json'

main(input_file, output_file)

import src.writer as writer
import src.reader as reader
import os

dir_string = "input"

directory = os.fsencode(dir_string)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    table = reader.read_contents(f"{dir_string}/{filename}")

for category in table.categories:
    writer.write(f"output/{category.name}.docx", f"{category.name}", category.contents)

os.rename("output/.docx", "output/original.docx")
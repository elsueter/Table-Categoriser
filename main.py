import writer, reader, os

table_001 = reader.read_contents("001.docx")

table_001 = merge_tables(table_001, table_002);

for category in table_001.categories:
    writer.write(f"output/{category.name}.docx", f"{category.name}", category.contents)
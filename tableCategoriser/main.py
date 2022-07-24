import writer, reader, os

table_001 = reader.read_contents("001.docx")
table_002 = reader.read_contents("002.docx")
table_003 = reader.read_contents("003.docx")
table_005 = reader.read_contents("005.docx")
table_006 = reader.read_contents("006.docx")
table_007 = reader.read_contents("007.docx")

table_001 = merge_tables(table_001, table_002);

for category in table_001.categories:
    writer.write(f"output/{category.name}.docx", f"{category.name}", category.contents)
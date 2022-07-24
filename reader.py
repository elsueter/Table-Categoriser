from docx import Document


class TableStructure:
    name = ""
    contents = []

    def __init__(self, input_name):
        self.name = input_name
        self.contents = []

    def push(self, input_array):
        self.contents.append(input_array)


class Tables:
    categories = [
        TableStructure("Triggers"),
        TableStructure("Blocks"),
        TableStructure("Therapist Shame"),
        TableStructure("with Shame"),
        TableStructure("Qualities of Therapist"),
        TableStructure("Other")
    ]

    def push(self, input_category, input_array):
        hit = False
        for category in self.categories:
            if category.name.lower() in input_category.lower():
                category.push(input_array)
                hit = True
        if not hit:
            self.categories[5].push(input_array)

    def print(self, input_category):
        print(f"Printing {input_category}:\n")
        for category in self.categories:
            if input_category == category.name:
                for row in category.contents:
                    print(row)



def read_contents(document_name):
    word_doc = Document(document_name)

    document_table = Tables()

    for table in word_doc.tables:
        for row in table.rows:
            temp_array = []
            for cell in row.cells:
                temp_array.append(cell.text)
            document_table.push(temp_array[2], temp_array)


    return document_table

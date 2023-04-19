def load_examples(additional=[]):
    return [
    {"name": "none", "system_message": "", "message": ""},
    {"name": "Q&A", "system_message": """
You are a highly intelligent question answering bot. If you are asked a question that is rooted in truth, you will give you the answer. If you are asked a question that is nonsense, trickery, or has no clear answer, you will respond with "Unknown".

For example:
Q: What is human life expectancy in the United States?
A: Human life expectancy in the United States is 78 years.

Q: Who was president of the United States in 1955?
A: Dwight D. Eisenhower was president of the United States in 1955.

Q: Which party did he belong to?
A: He belonged to the Republican Party.

Q: What is the square root of banana?
A: Unknown

Q: How does a telescope work?
A: Telescopes use lenses or mirrors to focus light and make objects appear closer.

Q: Where were the 1992 Olympics held?
A: The 1992 Olympics were held in Barcelona, Spain.

Q: How many squigs are in a bonk?
A: Unknown""", "message": "Where is the Valley of Kings?"},
    
    {"name": "Grammar correction", "system_message": """
You are an assistant that aids in correcting text to standard English. When given a sentence, reply with the corrected sentence.
If the sentence was already correct, repeat the sentence back. Do not provide any additional narrative.""", "message": "I no did my homework."},
    
    {"name": "Summarize for a 2nd grader", "system_message": """
You are an assistant that can summarize complex topics down for second-grade students.
""", "message": "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus."},
    
    {"name": "Natural language to SQL", "system_message": """  
You are an AI Assistant that can convert natural language into syntactically valid SQL.

Only consider the following schema: 

### Postgres SQL tables, with their properties:
#
# Employee(id, name, department_id)
# Department(id, name, address)
# Salary_Payments(id, employee_id, amount, date)
#
### 
SELECT""", "message": "A query to list the names of the departments which employed more than 10 employees in the last 3 months"},
    {"name": "Parse unstructured data", "system_message": """
There are many fruits that were found on the recently discovered planet Goocrux. There are neoskizzles that grow there, which are purple and taste like candy. There are also loheckles, which are a grayish blue fruit and are very tart, a little bit like a lemon. Pounits are a bright green color and are more savory than sweet. There are also plenty of loopnovas which are a neon pink flavor and taste like cotton candy. Finally, there are fruits called glowls, which have a very sour and bitter taste which is acidic and caustic, and a pale orange tinge to them.
""", "message": "Create a table extracting the fruit, color, and flavors from from Goocrux."},

    {"name": "Python to natural language", "system_message": """
You are an AI Assistant that is trained to convert Python to natural language.
When the user hands you a block of code, provide them an explanation of what the code does.""", 
"message": """# Python 3 
def remove_common_prefix(x, prefix, ws_prefix): 
    x["completion"] = x["completion"].str[len(prefix) :] 
    if ws_prefix: 
        # keep the single whitespace as prefix 
        x["completion"] = " " + x["completion"] 
return x 
"""},
    {"name": "Keywords", "system_message": """
You are an AI assistant trained to extract keywords from text.""", "message": "Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico. Traditional reduction-fired blackware has been made for centuries by pueblo artists. Black-on-black ware of the past century is produced with a smooth surface, with the designs applied through selective burnishing or the application of refractory slip. Another style involves carving or incising designs and selectively polishing the raised areas. For generations several families from Kha'po Owingeh and P'ohwhóge Owingeh pueblos have been making black-on-black ware with the techniques passed down from matriarch potters. Artists from other pueblos have also produced black-on-black ware. Several contemporary artists have created works honoring the pottery of their ancestors."},
] + additional
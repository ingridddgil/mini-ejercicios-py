questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "Berlin","Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Wich language is primarly spoken in Brazil?",
        "options": ["A) Spanish", "B) Portuguese", "C) English", "D) French"],
        "answer": "B"

    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A) 1", "B) 2", "C) 3", "D) 5"]
        "answer": "B"
    },
    {
        "prompt": "Who sings 'EoO'?"
        "optionns": ["A) Rauw alejandro", "B) Bad bunny", "C) Myke Towers", "D) Anitta"]
        "answer": "B"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)


run_quiz(questions)
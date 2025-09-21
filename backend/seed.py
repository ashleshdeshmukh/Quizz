from backend.app import app, db
from backend.models import Quiz, Question

def seed_data():
    with app.app_context():
        print("Using DB:", app.config["SQLALCHEMY_DATABASE_URI"])
        db.create_all()

        # Prevent duplicate seeding
        if Quiz.query.count() > 0:
            print("Database already has quizzes, skipping seeding")
            return

        # Define quizzes and their Aquestions
        quizzes = [
            {
                "title": "Python Quiz",
                "questions": [
                    {
                        "question": "Which keyword is used to define a function in Python?",
                        "options": ["func", "define", "def", "function"],
                        "answer": "def"
                    },
                    {
                        "question": "What is the output of: print(type([]))?",
                        "options": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"],
                        "answer": "<class 'list'>"
                    },
                    {
                        "question": "Which of the following is immutable in Python?",
                        "options": ["list", "set", "dict", "tuple"],
                        "answer": "tuple"
                    },
                    {
                        "question": "What is the correct file extension for Python files?",
                        "options": [".py", ".python", ".pyt", ".pt"],
                        "answer": ".py"
                    },
                    {
                        "question": "Which built-in function is used to get the length of a list?",
                        "options": ["count()", "size()", "len()", "length()"],
                        "answer": "len()"
                    },
                    {
                        "question": "What is the index of the first element in a Python list?",
                        "options": ["0", "1", "-1", "Depends"],
                        "answer": "0"
                    },
                    {
                        "question": "Which operator is used for exponentiation in Python?",
                        "options": ["^", "**", "exp()", "pow"],
                        "answer": "**"
                    },
                    {
                        "question": "Which module is used for generating random numbers in Python?",
                        "options": ["math", "random", "os", "time"],
                        "answer": "random"
                    },
                    {
                        "question": "Which keyword is used to handle exceptions?",
                        "options": ["try", "catch", "except", "throw"],
                        "answer": "except"
                    },
                    {
                        "question": "What will print(2 == 2.0) output?",
                        "options": ["True", "False", "Error", "None"],
                        "answer": "True"
                    }
                ]
            },
            {
                "title": "Java Quiz",
                "questions": [
                    {
                        "question": "Which keyword is used to inherit a class in Java?",
                        "options": ["extends", "inherits", "implements", "super"],
                        "answer": "extends"
                    },
                    {
                        "question": "What is the size of an int in Java?",
                        "options": ["16 bits", "32 bits", "64 bits", "Depends on OS"],
                        "answer": "32 bits"
                    },
                    {
                        "question": "Which method is the entry point of any Java program?",
                        "options": ["start()", "init()", "main()", "run()"],
                        "answer": "main()"
                    },
                    {
                        "question": "Which of these is not a Java primitive type?",
                        "options": ["int", "float", "boolean", "string"],
                        "answer": "string"
                    },
                    {
                        "question": "What is the default value of a boolean in Java?",
                        "options": ["true", "false", "0", "null"],
                        "answer": "false"
                    },
                    {
                        "question": "Which keyword is used to create an object in Java?",
                        "options": ["create", "alloc", "new", "instance"],
                        "answer": "new"
                    },
                    {
                        "question": "Which collection class allows duplicates and maintains insertion order?",
                        "options": ["HashSet", "ArrayList", "HashMap", "TreeSet"],
                        "answer": "ArrayList"
                    },
                    {
                        "question": "Which keyword is used to prevent inheritance?",
                        "options": ["static", "final", "private", "abstract"],
                        "answer": "final"
                    },
                    {
                        "question": "Which package is imported by default in every Java program?",
                        "options": ["java.util", "java.lang", "java.io", "java.net"],
                        "answer": "java.lang"
                    },
                    {
                        "question": "Which loop in Java is guaranteed to run at least once?",
                        "options": ["for", "while", "do-while", "foreach"],
                        "answer": "do-while"
                    }
                ]
            },
            {
                "title": "C++ Quiz",
                "questions": [
                    {
                        "question": "Which operator is used to allocate memory dynamically in C++?",
                        "options": ["malloc", "alloc", "new", "create"],
                        "answer": "new"
                    },
                    {
                        "question": "Who is the creator of C++?",
                        "options": ["Dennis Ritchie", "James Gosling", "Bjarne Stroustrup", "Guido van Rossum"],
                        "answer": "Bjarne Stroustrup"
                    },
                    {
                        "question": "Which header file is needed for input and output in C++?",
                        "options": ["<stdio.h>", "<iostream>", "<fstream>", "<string>"],
                        "answer": "<iostream>"
                    },
                    {
                        "question": "Which keyword is used to define a constant in C++?",
                        "options": ["const", "final", "define", "static"],
                        "answer": "const"
                    },
                    {
                        "question": "Which operator is overloaded for object output in C++?",
                        "options": ["<<", ">>", "::", "->"],
                        "answer": "<<"
                    },
                    {
                        "question": "Which of the following is not a valid C++ data type?",
                        "options": ["int", "float", "real", "char"],
                        "answer": "real"
                    },
                    {
                        "question": "Which function is the entry point of a C++ program?",
                        "options": ["start()", "init()", "main()", "program()"],
                        "answer": "main()"
                    },
                    {
                        "question": "Which keyword is used to inherit a base class in C++?",
                        "options": ["inherits", "extends", "base", "public"],
                        "answer": "public"
                    },
                    {
                        "question": "What is the size of a double in most C++ compilers?",
                        "options": ["4 bytes", "8 bytes", "16 bytes", "Depends"],
                        "answer": "8 bytes"
                    },
                    {
                        "question": "Which feature of C++ allows defining multiple functions with the same name but different parameters?",
                        "options": ["Overloading", "Overriding", "Encapsulation", "Polymorphism"],
                        "answer": "Overloading"
                    }
                ]
            }
        ]

        # Seed each quiz and its questions
        for qz in quizzes:
            quiz = Quiz(title=qz["title"])
            db.session.add(quiz)
            db.session.flush()  # ensures quiz.id is available

            for q in qz["questions"]:
                question = Question(
                    quiz_id=quiz.id,
                    question_text=q["question"],
                    options=q["options"],
                    correct_answer=q["answer"]
                )
                db.session.add(question)

        db.session.commit()
        print(" Database seeded with multiple quizzes and questions")

if __name__ == "__main__":
    seed_data()

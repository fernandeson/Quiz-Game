import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

# question_data = [
#     {"category": "Sports", "type": "boolean", "difficulty": "easy",
#      "question": "Manchester United won the 2013-14 English Premier League.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Sports", "type": "boolean", "difficulty": "medium",
#      "question": "Soccer player Cristiano Ronaldo opened a museum dedicated to himself.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Sports", "type": "boolean", "difficulty": "medium",
#      "question": "Skateboarding will be included in the 2020 Summer Olympics in Tokyo.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Sports", "type": "boolean", "difficulty": "medium",
#      "question": "The Olympics tennis court is a giant green screen.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Sports", "type": "boolean", "difficulty": "easy",
#      "question": "Roger Federer is a famous soccer player.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Sports", "type": "boolean", "difficulty": "medium",
#      "question": "Formula E is an auto racing series that uses hybrid electric race cars.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Sports", "type": "boolean", "difficulty": "easy",
#      "question": "In association football, or soccer, a corner kick is when the game restarts after someone scores
#      a goal.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Sports", "type": "boolean", "difficulty": "easy",
#      "question": "In Rugby League, performing a &quot;40-20&quot; is punished by a free kick for the opposing team.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "Sports", "type": "boolean", "difficulty": "medium",
#      "question": "Wilt Chamberlain scored his infamous 100-point-game against the New York Knicks in 1962.",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "Sports", "type": "boolean", "difficulty": "medium",
#      "question": "In 2008, Usain Bolt set the world record for the 100 meters with one shoelace untied.",
#      "correct_answer": "True", "incorrect_answers": ["False"]}]

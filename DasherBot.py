import random
import datetime
import time

class DasherBot:
    def __init__(self):
        self.name = "Dasher"
        self.energy = 100
        self.mood = "happy"
        self.points = 0
        
        self.responses = {
            "hi": [
                "Hello! Ready for adventure! ⚡", 
                "Hi there! Let's chat! 🌟", 
                "Hey! Great to see you! ✨"
            ],
            "how are you": [
                "Full of energy and ready to help! 🚀", 
                "I'm having a wonderful time! How about you? 💫", 
                "Feeling amazing! Let's do something fun! ⭐"
            ],
            "tell me a joke": [
                "Why don't computers wear shoes? Because they have a boot inside! 😄",
                "What did the robot do at lunchtime? Had a byte to eat! 🤖",
                "Why was the math book sad? Because it had too many problems! 📚",
                "Why did the cookie go to the doctor? Because it was feeling crumbly! 🍪",
                "What did one wall say to the other wall? I'll meet you at the corner! 🏠",
                "Why don't eggs tell jokes? They'd crack up! 🥚",
                "What do you call a bear with no teeth? A gummy bear! 🐻"
            ],
            "sing a song": [
                "🎵 Last Christmas, I gave you my heart!\nBut the very next day, you gave it away!\nThis year, to save me from tears\nI'll give it to someone special! 🎄",
                "🎵 Beep beep boop,\nI'm a singing robot,\nBeep beep boop,\nMaking music all day long! 🎶",
                "🎵 Do-Re-Mi,\nI'm as happy as can be,\nFa-So-La,\nLet's sing together, ha ha ha! 🎼"
            ],
            "find a recipe": [
                "Here's a simple sandwich recipe:\n1. Toast bread 🍞\n2. Add mayo\n3. Layer lettuce, tomato, cheese 🧀\n4. Top with second slice\n5. Enjoy! ✨",
                "Quick pasta recipe:\n1. Boil pasta 🍝\n2. Mix with sauce\n3. Add cheese\n4. Season to taste\n5. Ready to eat! 👨‍🍳",
                "Easy cookie recipe:\n1. Mix butter and sugar 🧈\n2. Add flour and eggs\n3. Make small balls\n4. Bake at 350°F\n5. Cool and enjoy! 🍪"
            ],
            "recommendation": [
                "You should watch Star Wars! It's epic! 🎬",
                "Why not try cooking something new? (and watching Star Wars?) 🍳",
                "How about going for a walk in the park? (then watch Star Wars!) 🌳",
                "Read a good book today! 📚",
                "Learn a new programming language! 💻",
                "Try meditation for 5 minutes! 🧘‍♂️",
                "Draw something creative! 🎨"
            ],
            "bye": [
                "Goodbye! You earned {points} points today! 👋",
                "See you next time! Your score: {points} ✨",
                "Bye! Come back soon! Points earned: {points} 🌟"
            ]
        }

        self.games = {
            "number": "Guess a number between 1-10! 🎲",
            "riddle": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. I have roads, but no cars. What am I? 🤔",
            "word": "Let's play word chain! I'll start with: Python 🐍"
        }

        self.game_answers = {
            "riddle": "map"
        }

    def play_game(self, game_type):
        if game_type == "number":
            secret = random.randint(1, 10)
            guess = input("Enter your guess (1-10): ")
            if guess.isdigit() and int(guess) == secret:
                self.points += 5
                return "You got it! +5 points! 🎉"
            return f"Not quite! It was {secret}. Try again! 🎲"

        elif game_type == "riddle":
            answer = input("Your answer: ").lower()
            if answer == self.game_answers["riddle"]:
                self.points += 10
                return "Correct! +10 points! 🎯"
            return "Not quite! The answer was 'map'. 🗺️"

        elif game_type == "word":
            word = input("Enter a word that starts with 'n': ")
            if word.lower().startswith('n'):
                self.points += 3
                return f"Nice word! +3 points! 📝"
            return "Word must start with 'n'! Try again! ✍️"

    def get_current_time(self):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"It's {current_time} ⏰"

    def get_weather(self, location):
        weathers = ["sunny ☀️", "rainy 🌧️", "cloudy ☁️", "snowy 🌨️"]
        temp = random.randint(0, 30)
        return f"In {location} it's {random.choice(weathers)} and {temp}°C"

    def get_response(self, user_input):
        user_input = user_input.lower()
        
        if "game" in user_input:
            game_type = random.choice(list(self.games.keys()))
            return self.games[game_type]

        if "current time" in user_input:
            return self.get_current_time()

        if "weather" in user_input:
            location = user_input.split("weather", 1)[-1].strip() or "your area"
            return self.get_weather(location)

        for key in self.responses:
            if key in user_input:
                response = random.choice(self.responses[key])
                return response.format(points=self.points)

        self.points += 1
        return random.choice([
            "Tell me more! +1 point for chatting! ",
            "That's interesting! +1 point! ",
            "Cool! Keep talking! +1 point! "
        ])

def main():
    bot = DasherBot()
    print(f"{bot.name}: Hi! I'm {bot.name}! Let's chat and play games! 🎮")
    print(f"{bot.name}: You can earn points by chatting and playing games! 🎯")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "bye":
            print(f"{bot.name}: {random.choice(bot.responses['bye']).format(points=bot.points)}")
            break
        
        response = bot.get_response(user_input)
        print(f"{bot.name}: {response}")
        
        if any(game in response for game in bot.games.values()):
            game_response = bot.play_game(next(key for key, value in bot.games.items() if value == response))
            print(f"{bot.name}: {game_response}")

if __name__ == "__main__":
    main()
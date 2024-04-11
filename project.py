import random
import string

class Markov:
    def __init__(self, order=3):
        self.order = order
        self.chain = {}

    def train(self, text):
        words = text.split()
        for i in range(len(words) - self.order):
            key = tuple(words[i:i + self.order])
            next_word = words[i + self.order]
            if key in self.chain:
                self.chain[key].append(next_word)
            else:
                self.chain[key] = [next_word]

    def generate_text(self, length=20):
        start = random.choice(list(self.chain.keys()))

        current_key = start
        generated_text = list(current_key)

        for _ in range(length):
            if current_key in self.chain:
                next_word = random.choice(self.chain[current_key])
                generated_text.append(next_word)
                current_key = tuple(generated_text[-self.order:])
            else:
                break

        return ' '.join(generated_text)

if __name__ == "__main__":
    with open("chapter1.txt", "r", encoding="utf-8") as file:
        trainingText = file.read()

    response = Markov(order=3)
    trainingText = trainingText.translate(str.maketrans('', '', string.punctuation)).lower()
    response.train(trainingText)

    generated_text = response.generate_text(length=random.randint(10, 30))
    print("Generated text:")
    print(generated_text)







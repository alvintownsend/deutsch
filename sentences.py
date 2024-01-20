#!/usr/bin/env python3

from typing import Self
import random

# Sentences generated by OpenAI's GPT-3.5 model (ChatGPT)
# OpenAI GPT-3.5 model: https://www.openai.com/gpt-3
SIMPLE_SENTENCES = [
    "The cat is on the table.",
    "I like to read books.",
    "We go to school every day.",
    "She is my best friend.",
    "The sun is shining brightly.",
    "They live in a small house.",
    "My favorite color is blue.",
    "He plays the guitar very well.",
    "We eat dinner at 7 p.m.",
    "It's a beautiful day outside.",
    "Do you speak German?",
    "The dog is sleeping in the garden.",
    "She has a red car.",
    "We watch movies on weekends.",
    "I have two sisters and one brother.",
    "It's raining heavily today.",
    "He loves to play soccer.",
    "The birds are singing in the trees.",
    "My parents are coming home soon.",
    "She is wearing a green dress.",
    "Can you swim in the pool?",
    "I want to learn German.",
    "The pizza is delicious.",
    "We visit our grandparents often.",
    "What is your favorite food?",
    "I have a big backpack.",
    "He is a good student.",
    "The train is arriving at the station.",
    "I need a new pair of shoes.",
    "She is writing a letter to her friend.",
    "We are going on vacation next month.",
    "The flowers are blooming in the garden.",
    "He likes to play video games.",
    "The baby is sleeping peacefully.",
    "I have a cat and a dog.",
    "What time is it?",
    "We are going to the park tomorrow.",
    "She is cooking dinner in the kitchen.",
    "They are listening to music.",
    "My favorite subject is science.",
    "The computer is on the desk.",
    "He drives a blue car.",
    "She goes to the gym every morning.",
    "The mountains are covered in snow.",
    "We have a picnic in the park.",
    "My favorite season is autumn.",
    "They play tennis on weekends.",
    "I want to visit Germany one day.",
    "The teacher is writing on the whiteboard.",
    "It's a quiet neighborhood.",
    "Do you like to cook?",
    "The river flows through the city.",
    "He wears glasses to read.",
    "We go for a walk in the evening.",
    "She is studying for her exams.",
    "The clock is ticking loudly.",
    "My sister has a pet rabbit.",
    "They are celebrating a birthday party.",
    "The beach is crowded in the summer.",
    "He takes the bus to work.",
    "I enjoy listening to music.",
    "She has a green thumb for gardening.",
    "We visit the museum on Saturdays.",
    "The alarm clock wakes me up.",
    "He is fixing the broken chair.",
    "Do you like to go camping?",
    "The baby is crawling on the floor.",
    "We play board games together.",
    "She has a talent for painting.",
    "The restaurant serves delicious food.",
    "They are watching a movie at home.",
    "I have a collection of stamps.",
    "It's a hot day in July.",
    "We swim in the lake in summer.",
    "He reads a book before bedtime.",
    "She wears a hat to protect from the sun.",
    "They take a family photo every year.",
    "The butterfly lands on the flower.",
    "We ride bicycles in the park.",
    "Do you have a favorite movie?",
    "The cat is chasing a mouse.",
    "He is building a sandcastle on the beach.",
    "She plays the piano beautifully.",
    "We go shopping on Saturdays.",
    "It's a windy day in the city.",
    "I have a hobby of collecting coins.",
    "They go hiking in the mountains.",
    "The children are playing in the backyard.",
    "She speaks three languages fluently.",
    "We take a vacation every summer.",
    "The coffee is too hot to drink.",
    "He takes photographs as a hobby.",
    "She wears a necklace around her neck.",
    "We have a barbecue in the backyard.",
    "The stars are shining in the night sky.",
    "Do you like to go for a run?",
    "The cat is hiding under the bed.",
    "She has a talent for playing the violin.",
    "They are planting flowers in the garden.",
    "I enjoy watching the sunset.",
    "We take the bus to school.",
    "The birds are chirping in the morning.",
    "He wears a hat to block the sun.",
    "She has a green thumb for gardening.",
    "They celebrate Christmas with family.",
    "I play the guitar in a band.",
    "We go skiing in the winter.",
    "The river flows through the valley.",
    "She bakes cookies for special occasions.",
    "It's a cloudy day with no sun.",
    "Do you like to go fishing?",
    "The dog is fetching a ball.",
    "He is jogging in the park.",
    "We have a picnic in the backyard.",
    "My favorite color is purple.",
    "They visit the zoo on weekends.",
    "She teaches English at a school.",
    "The airplane is flying overhead.",
    "We ride bikes along the trail.",
    "It's a cold day in December.",
    "Do you enjoy hiking in the mountains?",
    "The cat is playing with a toy.",
    "He is fixing a leaky faucet.",
    "She takes a dance class.",
    "We watch a documentary on TV.",
    "The flowers bloom in spring.",
    "I have a passion for photography.",
    "They build sandcastles at the beach.",
    "She swims in the pool.",
    "We have a family reunion every year.",
    "The coffee is too bitter.",
    "He collects rare coins.",
    "She wears a scarf in the winter.",
    "They have a barbecue in the park.",
    "I like to read novels.",
    "The kids are playing in the snow.",
    "We go on a road trip.",
    "The stars twinkle at night.",
    "She speaks Spanish fluently.",
    "They go for a walk after dinner.",
    "He is painting a landscape.",
    "We eat ice cream in the summer.",
    "The clock is ticking loudly.",
    "She has a collection of stamps.",
    "They take a cruise vacation.",
    "I enjoy listening to classical music.",
    "The cat is sleeping on the windowsill.",
    "He plays video games in his free time.",
    "We plant vegetables in the garden.",
    "It's a windy day at the beach.",
]

# more from ChatGPT, output is odd but probably useful going forward:
# 
# Ich drink Kaffee in the morning. (I drink coffee in the morning.)
# Du read Bücher in the evening. (You read books in the evening.)
# Wir gehen to Arbeit every day. (We go to work every day.)
# Sie ist my Freundin. (She is my friend.)
# Die Sonne scheint hell. (The sun is shining brightly.)
# Es ist a schöner Tag outside. (It's a beautiful day outside.)
# Ich mag Blau. (I like blue.)
# Er spielt Gitarre sehr gut. (He plays the guitar very well.)
# Wir essen Abendessen um 7 Uhr. (We eat dinner at 7 p.m.)
# Du sprichst Deutsch. (You speak German.)
# Der Hund schläft im Garten. (The dog is sleeping in the garden.)
# Sie hat ein rotes Auto. (She has a red car.)
# Wir schauen Filme am Wochenende. (We watch movies on weekends.)
# Ich habe zwei Schwestern und einen Bruder. (I have two sisters and one brother.)
# Es regnet schwer heute. (It's raining heavily today.)
# Er liebt Fußball zu spielen. (He loves to play soccer.)
# Die Vögel singen in den Bäumen. (The birds are singing in the trees.)
# Meine Eltern kommen bald nach Hause. (My parents are coming home soon.)
# Sie trägt ein grünes Kleid. (She is wearing a green dress.)
# Kannst du im Pool schwimmen? (Can you swim in the pool?)
# Ich möchte Deutsch lernen. (I want to learn German.)
# Die Pizza schmeckt lecker. (The pizza is delicious.)
# Wir besuchen oft unsere Großeltern. (We visit our grandparents often.)
# Was ist dein Lieblingsessen? (What is your favorite food?)
# Ich habe einen großen Rucksack. (I have a big backpack.)
# Er ist ein guter Schüler. (He is a good student.)
# Der Zug kommt am Bahnhof an. (The train is arriving at the station.)
# Ich brauche ein neues Paar Schuhe. (I need a new pair of shoes.)
# Sie schreibt einen Brief an ihre Freundin. (She is writing a letter to her friend.)
# Wir gehen nächsten Monat in den Urlaub. (We are going on vacation next month.)
# Die Blumen blühen im Garten. (The flowers are blooming in the garden.)
# Er spielt gerne Videospiele. (He likes to play video games.)
# Das Baby schläft friedlich. (The baby is sleeping peacefully.)
# Ich habe eine Katze und einen Hund. (I have a cat and a dog.)
# Wie spät ist es? (What time is it?)
# Wir gehen morgen in den Park. (We are going to the park tomorrow.)
# Sie kocht Abendessen in der Küche. (She is cooking dinner in the kitchen.)
# Sie hören Musik. (They are listening to music.)
# Mein Lieblingsfach ist Naturwissenschaft. (My favorite subject is science.)
# Ich trinke Wasser. (I drink water.)

class SimpleSentence:
    """
    Throw out a random pre-generated sentence to practice translating.
    """
    def __init__(self) -> Self:
        """
        Constructor, nothing here that matters yet.
        """
        pass

    def generate(self) -> str:
        """
        Prints a simple sentence in English.

        Your job is to write/say/think the sentence in German.
        """
        print(f"{random.choice(SIMPLE_SENTENCES)}")

if __name__ == "__main__":
    ss = SimpleSentence()
    ss.generate()

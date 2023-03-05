import openai
import speech_recognition as sr
import pyttsx3

# Configurer une clé d'API valide
openai.api_key = "sk-K1rdYkDkXGh41FijEtawT3BlbkFJKP4Plj7CTIhdxXxGjBsUque"

# Initialiser le moteur de synthèse vocale
engine = pyttsx3.init()

while True:
    # Demander à l'utilisateur de saisir une recherche
    prompt = input("Tape ta question ('exit' pour sortir) : ")
    if prompt == "exit":
        break
    # Envoyer une requête à l'API de GPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Afficher la réponse gt1
    print(response["choices"][0]["text"])
    engine.say(response["choices"][0]["text"])
    engine.runAndWait()
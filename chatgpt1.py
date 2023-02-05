#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
import openai

# Configurer une clé d'API valide
openai.api_key = "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"


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

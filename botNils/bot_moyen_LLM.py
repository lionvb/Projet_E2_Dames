
import re
from groq import Groq
import json

client = Groq(api_key="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")

ma_liste = [10, 20, 30]

prompt = (
    f"Voici la liste Python : {ma_liste}\n"
    "Écris un code Python qui calcule la moyenne de cette liste et renvoie juste une réponse sous la forme : moyenne = ... "
    "c'est à dire qui additione tous les termes de cette liste et les divise par le n,ombre d'élément qu'il y a dedant"
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}]
)

response_text = response.choices[0].message.content


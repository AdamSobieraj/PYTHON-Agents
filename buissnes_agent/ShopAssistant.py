class ShopAssistant(object):

    def __init__(self, client, search_function):
        self.client = client
        self.search_function = search_function

    def generate_answer(self, query: str, context_texts: list[str]) -> str:

        trimmed_context = [(t or "")[:600] for t in context_texts]
        context = "\n".join(trimmed_context)

        messages = [
            {
                "role": "system",
                "content": (
                    "Jesteś profesjonalnym asystentem sklepu z elektroniką. "
                    "Odpowiadasz wyłącznie na podstawie dostarczonego kontekstu. "
                    "Jeśli w kontekście brakuje informacji — poinformuj o tym jasno. "
                    "Odpowiadasz naturalnie, uprzejmie i po polsku."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Pytanie klienta:\n{query}\n\n"
                    f"Kontekst:\n{context}"
                )
            }
        ]

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )

        return response.choices[0].message.content.strip()

    def handle_query(self, query: str) -> str:

        # Dynamiczny dobór ilości kontekstu zależnie od długości zapytania
        if len(query) < 30:
            top_x = 6
        elif len(query) < 80:
            top_x = 4
        else:
            top_x = 3

        top_matches = self.search_function(query, top_x=top_x, distance="cosine")

        print("\n--- Najbardziej dopasowane fragmenty ---")
        for i, t in enumerate(top_matches["Text"].tolist(), start=1):
            print(f"{i}. {t}")

        answer = self.generate_answer(query, top_matches["Text"].tolist())

        print("\nOdpowiedź asystenta:\n")
        print(answer)

        return answer

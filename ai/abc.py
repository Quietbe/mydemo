import openai

openai.api_key = "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"


class Gpt(object):

    def generate_text(self, prompt):
        completions = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.8,
            max_tokens=3000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        message = completions.choices[0].text.strip()
        return [message, completions]

# def generate_text(prompt):
#     completions = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=0.8,
#         max_tokens=1000,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0.6,
#         stop=[" Human:", " AI:"]
#     )
#     message = completions.choices[0].text.strip()
#     return message
#
# while True:
#     prompt = input("请输入问题:\n")
#     response = generate_text(prompt)
#     print(response)

import tiktoken

encoder=tiktoken.encoding_for_model("gpt-4o")
text="Hello , I am Pragyan"
tokens=encoder.encode(text);
print("Tokens:",tokens);

tokens=[13225, 1366, 357, 939, 118421, 10134]
decoded_text=encoder.decode(tokens);
print("Decoded Text:",decoded_text);
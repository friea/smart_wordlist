from transformers import GPT2LMHeadModel, GPT2Tokenizer
from threading import Thread

def tahmin(seed_words):
    model_name = "gpt2"  # veya "gpt2-medium", "gpt2-large", "gpt2-xl" gibi farklı boyutlarda modeller
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    input_text = f"Generate words associated with: {', '.join(seed_words)}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    output = model.generate(input_ids, max_length=100, num_return_sequences=1, temperature=0.7, do_sample=True)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    associated_words = [word.strip() for word in generated_text.split(',')]
    return associated_words

import itertools
import string

def generate_wordlist_for_word(word, output_file='wordlist.txt', use_numbers=False, use_special_chars=False):
    if not word:
        print("Hata: Geçersiz kelime.")
        return
    all_chars = []
    if use_numbers:
        all_chars += string.digits  # Sayı karakterleri
    if use_special_chars:
        all_chars += string.punctuation  # Özel karakterler

    combinations = itertools.product(all_chars, repeat=2)
    suffixes = [''.join(combination) for combination in combinations]

    with open("wordlist.txt", 'wb') as file:
        for suffix in suffixes:
            file.write(word + suffix + '\n')


    print(f"Wordlist oluşturuldu ve '{output_file}' dosyasına kaydedildi.")

def generate_wordlist(words, use_numbers=False, use_special_chars=False):
    for word in words:
        t = Thread(target=generate_wordlist_for_word, args=(word, use_numbers, use_special_chars))
        t.start()


def split_and_flatten(strings):
    result = []
    for string in strings:
        words = string.split()
        result.extend(words)

    return result

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import re
from transformers import pipeline

from transformers import BartForConditionalGeneration, BartTokenizer

def clean_strings(string_list):
    cleaned_strings = []
    for string in string_list:
        cleaned_string = re.sub(r'[^a-zA-Z0-9ğüşıöçĞÜŞİÖÇ]', '', string)
        cleaned_strings.append(cleaned_string)
    return cleaned_strings

def iliskili_kelimeleri_bul(kelime):
    url = "https://tr.wikipedia.org/w/api.php?action=query&prop=links&titles={kelime}&format=json"
    response = requests.get(url)

    if response.status_code != 200:
        return "İstek yapılamadı. Lütfen daha sonra tekrar deneyin."

    iliskili_kelimeler = set()
    data = response.json()
    pages = data['query']['pages']

    for page_id in pages:
        page = pages[page_id]
        if 'links' in page:
            for link in page['links']:
                iliskili_kelimeler.add(link['title'])

    return iliskili_kelimeler

def tek_kelimeler(dizi):
    kelime_set = set()
    for kelime_grubu in dizi:
        kelimeler = kelime_grubu.split()
        for kelime in kelimeler:
            kelime_set.add(kelime)

    tek_kelime_dizi = list(kelime_set)
    return clean_strings(tek_kelime_dizi)

def kelime_al(kelime):
    iliskili_kelimeler = iliskili_kelimeleri_bul(kelime)
    tek_kelime_dizi = tek_kelimeler(iliskili_kelimeler)
    return tek_kelime_dizi

from transformers import BartForConditionalGeneration, BartTokenizer

# Modeli ve tokenizer'ı yükle
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

print("Çıkmak için 'q' giriniz")
while(True):
    rel= input("İlgili kelime giriniz: ")
    if(rel != "q"):
        print(kelime_al(rel))
        # Cümleyi tokenize edin
        tokenized_input = tokenizer(rel, return_tensors="pt")

        # Modeli kullanarak etiket tahmini yapın
        output = model.generate(**tokenized_input)

        # Etiketleri decode edin
        decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)

        # Sonuçları ekrana yazdır
        print(decoded_output)
    else:
        break

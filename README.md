# Detect the language of the given text based on frequent words.


## Requirements 
~~~~
- python2.7 +
- https://github.com/6/stopwords-json (Stopwords for various languages in JSON format.)
~~~~

## Run the code:
~~~~
$ python detect_language.py --path_of_the_txt_file
~~~~

### Output:
~~~~
Language 
~~~~

## Example Result:

Input text= 'Wikidata is een gratis en open knowledge base die kan worden gelezen en bewerkt door zowel mensen als machines.
Wikidata fungeert als centrale opslag voor de gestructureerde gegevens van zijn Wikimedia zusterprojecten, waaronder Wikipedia, Wikivoyage, Wikisource en anderen.

Wikidata biedt ook ondersteuning voor veel andere sites en services dan alleen Wikimedia-projecten! De inhoud van Wikidata is beschikbaar onder een gratis licentie, geëxporteerd met behulp van standaardindelingen en kan worden gekoppeld aan andere open datasets op het gekoppelde gegevensweb.'

output:
~~~~
dutch
~~~~

#!/usr/bin/env python2.7+
__author__ = 'Debjit Paul'
__Purpose__= 'Detecting language of any text using a most frequent words (stop words)' 

import argparse
import re
import sys
import json

#----------------------------------------------------------------------
def _read_lines(filename):
  """ read line by line 
    @param text: path of the input file
    @type text: str
    
    @return: Text whose language need to be detected
    @rtype: list"""

  data = []
  with open(filename, 'rb') as f:
      for line in f:
         data.append(line)
  return data

#----------------------------------------------------------------------
def _calculate_languages_counts(text):
    """
    Calculate the stop words present in the given text for each languages and return a dictionary like {'french': 2, 'spanish': 4, 'english': 0}
    
    @param text: Text whose language want to be detected
    @type text: str
    
    @return: Dictionary with languages and unique stopwords seen in analyzed text
    @rtype: dict
    """

    languages_counts = {}

    '''
    Computing the number of times which language's stop words occured in a text and for how many times. 
    '''
    words=str(text).lower().split()
    count_eng=0
    count_spanish=0
    count_german=0
    count_bengali=0
    count_chinese=0
    count_czech=0
    count_french=0
    count_hindi=0
    count_polish=0
    count_dutch=0
    count_portugese=0
    count_latin=0
    count_greek=0
    count_russian=0
    count_arabic=0

    with open("/home/debjit/Desktop/stopwords-all.json", 'r') as f:
        stop_words = json.load(f)	
    for word in words:
        if word.decode('utf-8') in stop_words['en']:
            count_eng=count_eng+1
        if word.decode('utf-8') in stop_words['es']:
            count_spanish=count_spanish+1
        if word.decode('utf-8') in stop_words['de']:
            count_german=count_german+1
        if word.decode('utf-8') in stop_words['bn']:
            count_bengali=count_bengali+1
        if word.decode('utf-8') in stop_words['zh']:
            count_chinese=count_chinese+1
        if word.decode('utf-8') in stop_words['cs']:
            count_czech=count_czech+1
        if word.decode('utf-8') in stop_words['fr']:
            count_french=count_french+1
        if word.decode('utf-8') in stop_words['hi']:
            count_hindi=count_hindi+1
        if word.decode('utf-8') in stop_words['pl']:
            count_polish=count_polish+1
        if word.decode('utf-8') in stop_words['nl']:
            count_dutch=count_dutch+1
        if word.decode('utf-8') in stop_words['el']:
            count_greek=count_greek+1
        if word.decode('utf-8') in stop_words['ru']:
            count_russian=count_russian+1
        if word.decode('utf-8') in stop_words['pt']:
            count_portugese=count_portugese+1
        if word.decode('utf-8') in stop_words['la']:
            count_latin=count_latin+1    
        if word.decode('utf-8') in stop_words['ar']:
            count_arabic=count_arabic+1 

    languages_counts={'english':count_eng, 'spanish':count_spanish, 'german':count_german, 'bengali':count_bengali, 'french':count_french, 'dutch':count_dutch, 'portugese':count_portugese, 'polish': count_polish, 'greek': count_greek, 'chinese':count_chinese, 'latin': count_latin, 'russian':count_russian, 'hindi':count_hindi, 'arabic': count_arabic}
    
    return languages_counts

#----------------------------------------------------------------------
def detect_language(text):
    """
    Detecting the language of the text based on the frequent words(stop words)
    
    @param text: Text whose language need to be detected
    @type text: str
    
    @return: Language
    @rtype: str
    """
    
    ratios=_calculate_languages_counts(text)
    language = max(ratios.keys(), key=(lambda k: ratios[k]))
    if ratios[language]!=0:
      return language
    else:
      return "Which language is that ???"

#----------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("txtfile", help=".txt file containing the input text", nargs='?')
    args = parser.parse_args()
    text = _read_lines(args.txtfile)
    language = detect_language(text)
    print language


if __name__=='__main__':
   main()

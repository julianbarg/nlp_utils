import pandas as pd
import textract
from os import listdir

folder = '/home/julian/Documents/Downloaded Articles'

# Read in the pdfs
pdfs = listdir(folder)
texts = [str(textract.process(folder + "/" + pdf)) for pdf in pdfs]
lengths = [len(text) for text in texts]
dict = {'name': pdfs, 'text': texts, 'length': lengths}
df = pd.DataFrame(dict)

# Word count
df['wordcount'] = df['text'].str.split().str.len()

# Cleaning
df['name'] = df.name.str.replace(';', ',')

# Count keywords
df['attention'] = df.text.str.count('attention')

# Attention sentences
attention_sentences = df['text'].str.findall('[^.]* attention [^.]*\.')
attention_sentences = pd.DataFrame(attention_sentences.to_list(), columns=
                                   ['sentence_1', 'sentence_2', 'sentence_3',
                                    'sentence_4', 'sentence_5', 'sentence_6',
                                    'sentence_7', 'sentence_8', 'sentence_9',
                                    'sentence_10', 'sentence_11', 'sentence_12',
                                    'sentence_13', 'sentence_14', 'sentence_15',
                                    'sentence_16'
                                    ])
df = pd.concat([df, attention_sentences], axis=1)

# Attention paragraphs
attention_paragraphs = df['text'].str.findall(
    '[^(\n|\\n|\\\n|\\\\n)]* attention [^(\n|\\n|\\\n|\\\\n)]*')
attention_paragraphs = pd.DataFrame(attention_paragraphs.to_list(), columns=
                                    ['paragraph_1', 'paragraph_2', 'paragraph_3',
                                     'paragraph_4', 'paragraph_5', 'paragraph_6',
                                     'paragraph_7', 'paragraph_8', 'paragraph_9',
                                     'paragraph_10', 'paragraph_11', 'paragraph_12',
                                     'paragraph_13', 'paragraph_14', 'paragraph_15',
                                     'paragraph_16'
                                     ])
df = pd.concat([df, attention_paragraphs], axis=1)

text_cols = ['sentence_1', 'sentence_2', 'sentence_3', 'sentence_4', 'sentence_5',
             'sentence_6', 'sentence_7', 'sentence_8', 'sentence_9', 'sentence_10',
             'sentence_11', 'sentence_12', 'sentence_13', 'sentence_14', 'sentence_15',
             'sentence_16', 'paragraph_1', 'paragraph_2', 'paragraph_3', 'paragraph_4',
             'paragraph_5', 'paragraph_6', 'paragraph_7', 'paragraph_8', 'paragraph_9',
             'paragraph_10', 'paragraph_11', 'paragraph_12', 'paragraph_13',
             'paragraph_14']
test = df.apply(lambda x: x.str.split().str.join(' ') if x.name in text_cols else x)

# Save output
df.to_csv('output.csv')
df_small = df.drop(['text'], axis=1)
df_small.to_csv('output_small.csv')

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

# Cleaning
df['name'] = df.name.str.replace(';', ',')

# Count keywords
df['attention'] = df.text.str.count('attention')

# Save output
df.to_csv('output.csv')
df.to_csv('output_small.csv', columns=['name', 'length', 'attention'])
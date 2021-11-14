# AUTOGENERATED! DO NOT EDIT! File to edit: Document Sumarization.ipynb (unless otherwise specified).

__all__ = ['summarizer', 'summarize']

# Cell
from transformers import pipeline
import pandas as pd
from IPython.display import display,clear_output, HTML
from ipywidgets import interact

# Cell
summarizer = pipeline("summarization")

# Cell
@interact(id=(0, len(df)))
def summarize(id=20):
    text = df.iloc[id].abstract.strip()
    title = df.iloc[id].title
    su = summarizer(text, max_length=len(text.split()), min_length=30, do_sample=False)
    display(HTML(f"<h2>{title}</h2><br><h3>Summary:</h3><p>{su[0]['summary_text']}</p><h3>Abstract</h3><p>{text}</p>"))

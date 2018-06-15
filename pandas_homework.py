import pandas as pd
to_read = pd.read_csv('to_read.csv')
books = pd.read_csv('books.csv', index_col='book_id')
book_tags = pd.read_csv('book_tags.csv')
tags = pd.read_csv('tags.csv', encoding='utf-8')
for i in books.columns:
    if i == 'goodreads_book_id' or i == 'title':
        continue
    else:
        del books[i]
book_needed = to_read.groupby('book_id').size()
book_popu = book_needed.sort_values(ascending=False)
fifty_mostwanted = book_popu.iloc[0:50]
fifty_books = books[books.index.isin(fifty_mostwanted.index)]
fifty_books['title'].to_csv('最热门五十本书.csv')
result = pd.merge(book_tags, fifty_books, left_on='_goodreads_book_id_', right_on='goodreads_book_id')
result = result.groupby('tag_id').sum().sort_values(by='count', ascending=False)[0:10]
top10_tags = pd.merge(result, tags, left_index=True, right_on='tag_id')
top10_tags['tag_name'].to_csv('最热门十大标签.csv')

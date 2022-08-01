import streamlit as st
import pandas as pd
import numpy as np
import pickle

popular = pickle.load(open('popular.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
similarity_scores = pickle.load(open("similarity_scores.pkl", 'rb'))

st.sidebar.title('My Book Recommender')
user_menu = st.sidebar.radio('Select an Option', ('Home', 'Recommend'))

if user_menu == 'Home':

    st.title("Top 20 Books")
    book_name = list(popular['Book-Title'].values)
    author = list(popular['Book-Author'].values)
    image = list(popular['Image-URL-M'].values)
    votes = list(popular['num_ratings'].values)
    rating = list(popular['avg_rating'].values)

    for i in range(20):
        if i % 4 == 0:
            col1, col2, col3, col4 = st.columns(4)
        if i % 4 == 0:
            with col1:
                st.image(image[i])
                st.write(book_name[i])
                st.write(author[i])
                st.write('No. of ratings ', votes[i])
                st.write('Avg. rating ', round(rating[i], 2))
        if i % 4 == 1:
            with col2:
                st.image(image[i])
                st.write(book_name[i])
                st.write(author[i])
                st.write('No. of ratings ', votes[i])
                st.write('Avg. rating ', round(rating[i], 2))
        if i % 4 == 2:
            with col3:
                st.image(image[i])
                st.write(book_name[i])
                st.write(author[i])
                st.write('No. of ratings ', votes[i])
                st.write('Avg. rating ', round(rating[i], 2))
        if i % 4 == 3:
            with col4:
                st.image(image[i])
                st.write(book_name[i])
                st.write(author[i])
                st.write('No. of ratings ', votes[i])
                st.write('Avg. rating ', round(rating[i], 2))

if user_menu == 'Recommend':
    st.title('Book Recommendation')
    book_name = st.selectbox('Book Name', sorted(
        popular['Book-Title'].unique()))

    if st.button('Submit'):
        index = np.where(pt.index == book_name)[0][0]

        similar_items = sorted(
            list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates(
                'Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates(
                'Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates(
                'Book-Title')['Image-URL-M'].values))

            data.append(item)

        col1, col2, col3, col4 = st.columns(4)
        for i in range(4):
            if i % 4 == 0:
                with col1:
                    st.image(data[i][2])
                    st.write(data[i][0])
                    st.write(data[i][1])

            if i % 4 == 1:
                with col2:
                    st.image(data[i][2])
                    st.write(data[i][0])
                    st.write(data[i][1])

            if i % 4 == 2:
                with col3:
                    st.image(data[i][2])
                    st.write(data[i][0])
                    st.write(data[i][1])

            if i % 4 == 3:
                with col4:
                    st.image(data[i][2])
                    st.write(data[i][0])
                    st.write(data[i][1])

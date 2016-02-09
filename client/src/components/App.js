import React, { Component } from 'react'
import styles from '../styles/main.scss'
import bookData from '../../book_data.json'
import Book from './book/book';

export default class App extends Component {
  render() {
    console.log('book data: ', bookData);
    const books = bookData.map(book => {
      return <Book book={book} />
    })
    return (
      <div className="app">
        <h1>Read a book, a few pages at a time.</h1>
        {books}
      </div>
    );
  }
}

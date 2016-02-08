import React, { Component } from 'react';
import styles from './styles/main.scss'
import bookData from '../book_data.json'

export default class App extends Component {
  render() {
    console.log('book data: ', bookData);
    const books = bookData.map(book => {
      return <img src={book.cover_url} className="book" />
    })
    return (
      <div className="App">
        {books}
      </div>
    );
  }
}

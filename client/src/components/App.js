import React, { Component } from 'react'
import styles from '../styles/main.scss'
import bookData from '../../book_data_twenty.json'
import Book from './book/book';
import BookDetail from './book_detail/book_detail'

export default class App extends Component {
  constructor() {
    super()
    this.state = {
      selectedBook: null
    }
  }

  handleSelectBook = (book) => {
    this.setState({selectedBook:book})
  };

  handleDeselectBook = () => {
    this.setState({selectedBook:null})
  };

  renderSelectedBook = () => {
    const {selectedBook} = this.state
    if (selectedBook) {
      return <BookDetail book={selectedBook}
               onClose={this.handleDeselectBook}/>
    }
  };

  render() {
    const books = bookData.map((book, i) => (
      <Book book={book} key={i} onClick={this.handleSelectBook}/>))
    return (
      <div className="app">
        <h1>Read a book, a few pages at a time.</h1>
        {books}
        {this.renderSelectedBook()}
      </div>
    );
  }
}

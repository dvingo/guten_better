import React, { Component } from 'react'
import styles     from '../styles/main.scss'
import bookData   from '../../book_data_twenty.json'
import Book       from './book/book';
import BookDetail from './book_detail/book_detail'
import axios      from 'axios'
const postScheduleEnpoint = '/schedule'

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

  handleSubscription = (email) => {
    console.log('IN APP, got email: ', email);
    const {selectedBook} = this.state
    axios.post(postScheduleEnpoint, {
      email: email,
      gutenberg_id: selectedBook.guten_id
    })
    .then( () => {
      // TODO popup with success message to human.
    })
    .catch( () => {
      // TODO popup with failure message to human.
    })
    this.setState({selectedBook: null})
  };

  renderSelectedBook = () => {
    const {selectedBook} = this.state
    if (selectedBook) {
      return <BookDetail
               book={selectedBook}
               onSubmit={this.handleSubscription}
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

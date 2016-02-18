import React, { Component } from 'react'
import styles     from '../styles/main.scss'
import bookData   from '../../book_data_twenty.json'
import Alert      from './alert/alert'
import Book       from './book/book';
import BookDetail from './book_detail/book_detail'
import axios      from 'axios'
const postScheduleEnpoint = '/schedules'

export default class App extends Component {

  constructor() {
    super()
    this.state = {
      selectedBook: null,
      message: null
    }
  }

  handleSelectBook = (book) => {
    this.setState({selectedBook: book})
  };

  handleDeselectBook = () => {
    this.setState({selectedBook: null})
  };

  handleSubscription = (email) => {
    console.log('IN APP, got email: ', email);
    const {selectedBook} = this.state
    axios.post(postScheduleEnpoint, {
      email: email,
      gutenberg_id: selectedBook.guten_id
    }).then(() => {
      this.setState({
        message: 'Signup complete!',
        selectedBook: null
      })
    }).catch(() => {
      this.setState({
        message: 'Error trying to sign you up!',
        selectedBook: null
      })
    })
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

  renderMessage = () => {
    const {message} = this.state
    if (message) {
      return <Alert message={message} onClose={() => {
        this.setState({message: null})
      }} />
    }
  };

  render() {
    const books = bookData.map((book, i) => (
      <Book book={book} key={i} onClick={this.handleSelectBook}/>))
    return (
      <div className="app">
        <h1>Pick a book and we'll send you a few pages a day.</h1>
        {books}
        {this.renderMessage()}
        {this.renderSelectedBook()}
      </div>
    );
  }
}

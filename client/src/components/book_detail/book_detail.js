import React, { Component } from 'react'

export default class BookDetail extends Component {

  render() {
    const { cover_url: coverUrl, name } = this.props.book
    return (
      <div className="book-detail">
        <div className="book-detail__close" onClick={this.props.onClose}>✕</div>
        <div className="book-detail__container">
          <img className="book-detail__image" src={coverUrl} />
          <h1 className="book-detail__name">&ldquo;{name}&rdquo;</h1>
          <form onSubmit={this.props.onSubmit}>
          <input
            className="book-detail__email"
            type="text"
            placeholder="Enter your email address"/>

          <input type="submit"
            className="book-detail__submit"
            value="Read This Book" />
          </form>
        </div>
      </div>
    )
  }

}

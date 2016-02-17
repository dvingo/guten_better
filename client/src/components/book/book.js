import React, { Component } from 'react'

export default class Book extends Component {


  render() {
    const { cover_url: coverUrl, name } = this.props.book

    return (
      <div className="book">
        <div className="book__aspect-helper"></div>

        <div className="book__back-container">
          <div className="book__vertical-helper"></div>
          <img src={coverUrl} className="book__img"
               title={name} alt={name} />
        </div>

        <div className="book__front-container">
          <div className="book__vertical-helper"></div>
            <img src={coverUrl} className="book__img"
                 title={name} alt={name} onClick={this.props.onClick.bind(null, this.props.book)} />
        </div>
      </div>
    );
  }
}

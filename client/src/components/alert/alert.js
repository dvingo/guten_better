import React, { Component } from 'react'

export default class Alert extends Component {

  componentDidMount() {
    window.addEventListener('keyup', this.handleKeyPress)
  }

  componentWillUnmount() {
    window.removeEventListener('keyup', this.handleKeyPress)
  }

  handleKeyPress = (e) => {
    if (e.key === 'Escape') {
      this.props.onClose()
    }
  };

  render() {
    return (
      <div className="alert">

        <div className="alert__container">
          <h1 className="book-detail__name">
            {this.props.message}
          </h1>

          <button className="alert__button" onClick={this.props.onClose}>
            OK
          </button>
        </div>
      </div>
    )
  }

}

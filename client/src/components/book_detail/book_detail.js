import React, { Component } from 'react'

function isValidEmail(val) {
  var re = /[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,30}/i
  return re.test(val)
}

export default class BookDetail extends Component {
  constructor() {
    super()
    this.state = { error: null, email: null }
  }

  componentDidMount() {
    window.addEventListener('keyup', this.handleKeyPress)
  }

  componentWillUnmount() {
    window.removeEventListener('keyup', this.handleKeyPress)
  }

  handleOnSubmit = (e) => {
    e.preventDefault()
    this.setState({error: null})
    const {email} = this.state

    if (isValidEmail(email)) {
      this.props.onSubmit(email)
    } else {
      this.setState({error: 'Please enter a valid email address'})
    }
  };

  handleOnEmailChange = (e) => {
    e.preventDefault()
    this.setState({email: e.target.value})
  };

  renderError = () => {
    const {error} = this.state
    if (error) {
      return <p className="book-detail__error">{error}</p>
    }
  };

  handleKeyPress = (e) => {
    if (e.key === 'Escape') {
      this.props.onClose()
    }
  };

  render() {
    const { cover_url: coverUrl, name } = this.props.book
    return (
      <div className="book-detail">

        <div className="book-detail__close" onClick={this.props.onClose}>✕</div>

        <div className="book-detail__container">
          <img className="book-detail__image" src={coverUrl} />
          <h1 className="book-detail__name">&ldquo;{name}&rdquo;</h1>

          <form onSubmit={this.handleOnSubmit}>
          {this.renderError()}
          <input
            className="book-detail__email"
            type="text"
            value={this.state.email}
            placeholder="Enter your email address"
            onChange={this.handleOnEmailChange}/>

          <input type="submit"
            className="book-detail__submit"
            value="Read This Book" />
          </form>

        </div>
      </div>
    )
  }

}

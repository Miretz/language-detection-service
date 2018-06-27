import React, { Component } from 'react';
import axios from 'axios';

import './LanguageDetection.css';

class LanguageDetection extends Component {

  state = {
    text: '',
    results: {
      langdetect: {},
      langid: {},
      languagesDetected: [],
      length: 0,
      overallLanguage: '',
      text: ''
    }
  }

  handleChange = (e) => {

    this.setState({ text: e.target.value })

    const serviceInput = {
      text: this.state.text
    };

    axios.post(`http://localhost:5000/api/languages`, serviceInput)
      .then(res => {
        console.log(res);
        console.log(res.data);
        this.setState({ results: res.data })
      })
  }

  render() {
    const { text, results } = this.state
    const langs = results.languagesDetected.map((lang) =>
      <li key={lang}>
        {lang}
      </li>
    );

    return (
      <div>
        <textarea
          id={'id'}
          value={text}
          placeholder={'Enter your text here...'}
          onChange={this.handleChange}
        />
        <br />
        <br />
        Detected language:
        <div className="Language-result">
          Overall Language: {results.overallLanguage}
          <br />
          <ul>{langs}</ul>
        </div>
      </div>
    )
  }
}

export default LanguageDetection;
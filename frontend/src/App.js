import React, { Component } from 'react';
import './App.css';
import LanguageDetection from './LanguageDetection';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Language Detection</h1>
        </header>
        <LanguageDetection/>
      </div>
    );
  }
}

export default App;

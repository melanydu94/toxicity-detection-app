import logo from './logo.svg';
import { useEffect } from 'react';
import './App.css';

import SentenceForm from './SentenceForm';

function App() {
  useEffect(() => {
    fetch("/model").then(response =>
      console.log(response)
      ).then(jsonData => {
        console.log(jsonData)
      })
  }, [])
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <div>
          <h2>Sentiment analysis of the sentence</h2>
          <SentenceForm/>
        </div>
      </header>
      <footer>
        <p>Author: Melany Ebrahim, Louis Minart, Dany Sonethavy</p>
        <p>The application is a sentiment analysis application, which, given a piece of text, should be able to reply with its sentiment as being positive, negative, or neutral.</p>
      </footer>
    </div>
  );
}

export default App;

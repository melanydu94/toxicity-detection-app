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
          <h2>Toxicity detection of the sentence</h2>
          <SentenceForm/>
        </div>
      </header>
      <footer>
        <p>Author: Melany Ebrahim, Dany Sonethavy</p>
        <p>The application is a toxicity detection application, which, given a piece of text, should be able to detect different types of of toxicity like threats, obscenity, insults, and identity-based hate.</p>
      </footer>
    </div>
  );
}

export default App;

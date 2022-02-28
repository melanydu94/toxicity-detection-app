import logo from './petit_dauphin.gif'
import { useEffect } from 'react';
import './App.css';

import SentenceForm from './SentenceForm';

function App() {
  useEffect(() => {
    fetch("/model",
      {
        mode: 'no-cors',
        credentials: 'include',
        method: 'POST',
        headers: headers
    }
  ).then(response =>
      console.log(response)
      ).then(jsonData => {
        console.log(jsonData)
      })
  }, [])
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} alt="logo" width="300"/>
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

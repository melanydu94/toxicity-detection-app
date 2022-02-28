import React from 'react';
import axios from 'axios';
import GaugeChart from 'react-advanced-gauge-chart'

export default class SentenceForm extends React.Component {
  state = {
    my_sentence: '',
    my_sentiment: 'Undefined',
    my_pos_score: '0.0',
    my_neu_score: '0.0',
    my_neg_score: '0.0',
  }

  handleChange = event => {
    this.setState({ my_sentence: event.target.value })
  }

  handleSubmit = event => {
    event.preventDefault();

    const form = {
      sentence: this.state.my_sentence
    };

    axios.post(`http://127.0.0.1:5000/model`, form )
      .then(res => {
        console.log(res);
        console.log(res.data);
        this.setState({ my_pos_score: res.data.Rating_Positive });
        this.setState({ my_neu_score: res.data.Rating_Neutral });
        this.setState({ my_neg_score: res.data.Rating_Negative });
        this.setState({ my_sentiment: res.data.Sentiment });
      })

    
  }

  render() {
    return (
      <div>
          <div>
                <GaugeChart id="gauge-chart1" 
                    nrOfLevels={15} 
                    percent={this.state.my_neg_score} 
                    needleColor="#345243"
                    style={{width: "300px", display:'inline-block'}}
                    colors={["#FF0000"]}
                    className="row"
                />
                <GaugeChart id="gauge-chart2" 
                    nrOfLevels={15} 
                    percent={this.state.my_neu_score} 
                    needleColor="#345243"
                    style={{width: "300px", display:'inline-block'}}
                    colors={["#FFFFFF"]}
                    className="row"
                />
                <GaugeChart id="gauge-chart3" 
                    nrOfLevels={15} 
                    percent={this.state.my_pos_score} 
                    needleColor="#345243"
                    style={{width: "300px", display:'inline-block'}}
                    colors={["#00FF00"]}
                    className="row"
                />
        </div>
        <h2 id="sentiment">Overall : {this.state.my_sentiment}</h2>
        <form onSubmit={this.handleSubmit}>
          <label>
            Enter your sentence : &nbsp;
            <input type="text" name="sentence" onChange={this.handleChange} />
          </label>
          <br>
          </br>
          <button type="submit">Predict Sentiment</button>
        </form>
      </div>
    )
  }
}
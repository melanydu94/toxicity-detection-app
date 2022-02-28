import React from 'react';
import axios from 'axios';
import Chart from 'react-apexcharts'

export default class SentenceForm extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      my_sentence: '',
      series: [15, 15, 15, 15, 15, 15],
      options: {
        chart: {
          type: 'donut',
        },
        responsive: [{
          breakpoint: 480,
          options: {
            chart: {
              width: 200
            }
          }
        }],
        legend: {
          position: 'bottom',
          colors: '#ffffff',
          useSeriesColors: false
        },
        labels: ["toxicity", "severe_toxicity", "obscene", "threat", "insult", "identity_attack"],
        colors: ["#447b40", "#cc7870", "#e74ce4","#447b40", "#cc7870", "#e74ce4"]
      },
    
    
    };
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
        this.setState({ series: [res.data.toxicity, res.data.severe_toxicity, res.data.obscene, res.data.threat, res.data.insult, res.data.identity_attack] });
      })
  }

  render() {
    return (
      <div>
          <div>
            <form onSubmit={this.handleSubmit}>
            <label>
              Enter your sentence : &nbsp;
              <input type="text" name="sentence" onChange={this.handleChange} />
            </label>
            &nbsp;
            <button type="submit">Predict Sentiment</button>
          </form>
            <div id="chart">
              <Chart options={this.state.options} series={this.state.series} type="donut" width="600"/>
            </div>
        </div>
      </div>
    )
  }
}
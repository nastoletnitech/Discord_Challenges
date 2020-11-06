import React, {Component} from 'react';
import './App.css';
import randomColor from 'randomcolor';

export default class App extends Component {
    state = {
        squares: [],
        count: 6,
        type: "hex",
        info: "Choose one!",
        color: "",
        points: 0
    }

    getRandom(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    componentDidMount() {
        let squares = [];
        let colors = randomColor({format: this.state.type, count: this.state.count});
        for (let i = 0; i < this.state.count; i++) {
            squares.push({id: i, color: colors[i]});
        }
        this.setState({squares});
        this.setState({squares});
        let r = this.getRandom(0, this.state.count - 1);
        this.setState({color: colors[r]});
    }

    render() {
        const _click = id => {
            let square = this.state.squares.filter(s => {return s.id === id})[0];
            if(square.color === this.state.color) { this.componentDidMount(); this.render(); this.setState({points: this.state.points + 1}); this.setState({info: "OK! Choose one!"});}
            else { this.setState({info: "Try again!"}); this.setState({points: 0}); }
        }
        const _handleCount = e => {
            if(e.target.value < 2 || e.target.value > 10) {
                this.setState({info: "Give value between 2 and 10!"});
                return;
            }
            this.setState({info: "Choose one!"});
            this.setState({count: e.target.value || 6}, function () {
                this.componentDidMount();
            });
            this.componentDidMount();
        }
        const _handleType = e => {
            this.setState({type: e.target.value}, function () {
                this.componentDidMount();
            });
            this.componentDidMount();
        }
        return (
            <div className="app">
                <div className="app__header">
                    Hello, choose square with given color...
                </div>
                <div className="app__container">
                    <div className="app__container__color">
                        {this.state.color}
                    </div>
                    <div className="app__container__settings">
                        <strong><h2>Points: {this.state.points}</h2></strong>
                        <strong><h2>Settings</h2></strong>
                        <div className="count">
                            <strong><h3>Count</h3></strong>
                            <input type="text" onChange={_handleCount} placeholder="Enter count..."/>
                        </div>
                        <div className="type">
                            <strong><h3>Type</h3></strong>
                            <select value={this.state.type} onChange={_handleType}>
                                <option value="hex">HEX</option>
                                <option value="rgb">RGB</option>
                                <option selected value="hsl">HSL</option>
                            </select>
                        </div>
                    </div>
                    <div className="app__container__squares">
                        {this.state.squares.map(square => {
                            return <div className="square" style={{backgroundColor: square.color}} onClick={() => _click(square.id)} key={square.id} />
                        })}
                    </div>
                    <div className="app__container__info">
                        {this.state.info}
                    </div>
                </div>
            </div>
        );
    }
}

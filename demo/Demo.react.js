import React, {Component} from 'react';
import {WebcamComponent} from '../src';

class Demo extends Component {
    constructor() {
        super();
        this.state = {
            value: ''
        }
    }

    render() {
        return (
            <div>
                <h1>dash-webcam Demo</h1>

                <hr/>
                <h2>Webcam Component</h2>
                <WebcamComponent />
                <hr/>
            </div>
        );
    }
}

export default Demo;

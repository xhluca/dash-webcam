import React, {Component} from 'react';
import PropTypes from 'prop-types';
import Webcam from 'react-webcam';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class WebcamComponent extends Component {
    constructor(props) {
        super(props);
        this.getScreenshot = this.getScreenshot.bind(this);
        this.state = {value: props.value};
    }

    getScreenshot(){
        const {setProps} = this.props;
        // const screenshot = this.refs.webcam.getScreenshot();
        console.log('hello');

        if (setProps  !== null) {
            setProps({screenshot: 'hello world'});
        }
    }

    render() {
        const {
            className,
            audio,
            height,
            width,
            screenshotWidth,
            screenshotFormat,
            screenshotQuality
        } = this.props;

        return (
            <Webcam
                ref="webcam"
                className={className}
                audio={audio}
                height={height}
                width={width}
                screenshotWidth={screenshotWidth}
                screenshotFormat={screenshotFormat}
                screenshotQuality={screenshotQuality}
                getScreenshot={this.getScreenshot}
            />
        );
    }
}

WebcamComponent.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id: PropTypes.string,

    /**
     * CSS class of video element
     */
    className: PropTypes.string,

    /**
     * enable/disable audio
     */
    audio: PropTypes.boolean,

    /**
     * height of video element
     */
    height: PropTypes.number,

    /**
     * width of video element
     */
    width: PropTypes.number,

    /**
     * width of screenshot
     */
    screenshotWidth: PropTypes.number,

    /**
     * format of screenshot
     */
    screenshotFormat: PropTypes.string,

    /**
     * quality of screenshot(0 to 1)
     */
    screenshotQuality: PropTypes.number,

    /**
     * Dash-assigned callback that should be called whenever any of the
     * properties change
     */
    setProps: PropTypes.func,

    /**
     * Screenshots
     */
    screenshot: PropTypes.string,


    /**
     * Screenshots
     */
    getScreenshot: PropTypes.string
};

WebcamComponent.defaultProps = {
    audio: true,
    height: 480,
    width: 640,
    screnshotFormat: 'image/webp',
    screenshotQuality: 0.92
};
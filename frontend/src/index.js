import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import About from './containers/About/About';
import { BrowserRouter, Route } from 'react-router-dom';
import registerServiceWorker from './registerServiceWorker';

const app = (
    <BrowserRouter >
    <div>
        <Route path="/about" exact component={About} />
        <Route path="/" exact component={App} />
    </div>
    </BrowserRouter>

)
ReactDOM.render(app, document.getElementById('root'));
registerServiceWorker();

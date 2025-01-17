import React from 'react';  
import ReactDOM from 'react-dom/client';  
import { BrowserRouter as Router } from 'react-router-dom';  
import App from './App';  // Import the main App component  
  

const root = ReactDOM.createRoot(document.getElementById('root'));  

root.render(  
  <React.StrictMode>  
    <Router>  
      <App />  
    </Router>  
  </React.StrictMode>  
);
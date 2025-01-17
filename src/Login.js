import React, { useState } from 'react';  
import { Link } from 'react-router-dom';  // Import Link from react-router-dom  

function Login() {  
  const [email, setEmail] = useState('');  
  const [password, setPassword] = useState('');  
  const [feedback, setFeedback] = useState('');  

  const handleLogin = async (e) => {  
    e.preventDefault();  

    try {  
      const response = await fetch('http://127.0.0.1:8000/api/login/', {  
        method: 'POST',  
        headers: {  
          'Content-Type': 'application/json',  
        },  
        body: JSON.stringify({ email, password }),  
      });  

      if (!response.ok) {  
        throw new Error('Login failed');  
      }  

      const data = await response.json();  
      const token = data.token; // Assuming the API returns a token  
      localStorage.setItem('authToken', token); // Store token  
      setFeedback('Login successful!');  
    } catch (error) {  
      console.error('Error during login:', error);  
      setFeedback('Error during login. Please try again.');  
    }  
  };  

  return (  
    <div className="container">  
      <h2>Login</h2>  
      {feedback && <p className="alert alert-info">{feedback}</p>}  
      <form onSubmit={handleLogin}>  
        <div className="mb-3">  
          <label htmlFor="email" className="form-label">Email:</label>  
          <input  
            type="email"  
            id="email"              // Unique ID  
            name="email"            // Added name attribute  
            value={email}  
            onChange={(e) => setEmail(e.target.value)}  
            className="form-control"  
            required  
          />  
        </div>  
        <div className="mb-3">  
          <label htmlFor="password" className="form-label">Password:</label>  
          <input  
            type="password"  
            id="password"           // Unique ID  
            name="password"         // Added name attribute  
            value={password}  
            onChange={(e) => setPassword(e.target.value)}  
            className="form-control"  
            required  
          />  
        </div>  
        <button type="submit" className="btn btn-primary">Login</button>  
      </form>  
      <p className="mt-3">  
        Don't have an account?{' '}  
        <Link to="/register" className="btn btn-link">Register Here</Link>  {/* Link to registration page */}  
      </p>  
    </div>  
  );  
}  

export default Login;
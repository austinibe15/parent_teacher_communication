import React, { useState } from 'react';  

function Register() {  
  const [name, setName] = useState('');  
  const [email, setEmail] = useState('');  
  const [password, setPassword] = useState('');  
  const [feedback, setFeedback] = useState('');  

  const handleRegister = async (e) => {  
    e.preventDefault();  

    try {  
      const response = await fetch('http://127.0.0.1:8000/api/register/', {  
        method: 'POST',  
        headers: {  
          'Content-Type': 'application/json',  
        },  
        body: JSON.stringify({ name, email, password }),  
      });  

      if (!response.ok) {  
        throw new Error('Registration failed');  
      }  

      const data = await response.json();  
      setFeedback('Registration successful! Please log in.');  
      // Optionally redirect or clear the form  
      setName('');  
      setEmail('');  
      setPassword('');  
    } catch (error) {  
      console.error('Error during registration:', error);  
      setFeedback('Error during registration. Please try again.');  
    }  
  };  

  return (  
    <div className="container">  
      <h2>Register</h2>  
      {feedback && <p className="alert alert-info">{feedback}</p>}  
      <form onSubmit={handleRegister}>  
        <div className="mb-3">  
          <label htmlFor="name" className="form-label">Name:</label>  
          <input  
            type="text"  
            id="name"  // Unique ID  
            name="name"  // Unique name  
            value={name}  
            onChange={(e) => setName(e.target.value)}  
            className="form-control"  
            required  
          />  
        </div>  
        <div className="mb-3">  
          <label htmlFor="email" className="form-label">Email:</label>  
          <input  
            type="email"  
            id="email"  // Unique ID  
            name="email"  // Unique name  
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
            id="password"  // Unique ID  
            name="password" // Unique name  
            value={password}  
            onChange={(e) => setPassword(e.target.value)}  
            className="form-control"  
            required  
          />  
        </div>  
        <button type="submit" className="btn btn-primary">Register</button>  
      </form>  
    </div>  
  );  
}  

export default Register;
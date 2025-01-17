import React, { useState } from 'react';  

function SendMessage() {  
  const [content, setContent] = useState("");  

  const handleSubmit = (e) => {  
    e.preventDefault();  
    // Logic to send the message, e.g., API call  
    console.log("Message sent:", content);  
    setContent("");  // Clear input field after sending  
  };  

  return (  
    <div>  
      <h2>Send a Message</h2>  
      <form onSubmit={handleSubmit}>  
        <div className="mb-3">  
          <label htmlFor="messageContent" className="form-label">Message:</label>  
          <input  
            type="text"  
            id="messageContent"  // Unique ID  
            name="messageContent"  // Unique name  
            value={content}  
            onChange={(e) => setContent(e.target.value)}  
            className="form-control"  
            required  
          />  
        </div>  
        <button type="submit" className="btn btn-primary">Send</button>  
      </form>  
    </div>  
  );  
}  

export default SendMessage;
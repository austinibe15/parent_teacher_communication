import React from 'react';  

const Announcements = () => {  
  return (  
    <div className="announcements my-5">  
      <h2 className="text-center">Announcements & Events</h2>  
      <div className="row">  
        {/* Sample Event Card */}  
        <div className="col-md-6">  
          <div className="card mb-3">  
            <div className="card-body">  
              <h5 className="card-title">Upcoming Event: Parent-Teacher Conference</h5>  
              <p>Date: February 15, 2025</p>  
              <p>Description: Join us for the Parent-Teacher Conference to discuss your child's progress.</p>  
              <button className="btn btn-primary">RSVP</button>  
            </div>  
          </div>  
        </div>  
        {/* Additional announcement cards go here */}  
      </div>  
    </div>  
  );  
}  

export default Announcements;
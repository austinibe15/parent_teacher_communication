import React from 'react';  
import { Route, Link, Routes } from 'react-router-dom';  
import Register from './Register';  
import Login from './Login';  // Import the Login component  
import MessagesList from './SendMessages'; // Ensure this file exists  

const App = () => {  
    return (  
        <div className="d-flex flex-column min-vh-100">  
            <header className="bg-light p-3">  
                <h1 className="text-center">Parent-Teacher Communication App</h1>  
            </header>  
            <div className="d-flex flex-grow-1">  
                <nav className="nav flex-column bg-light p-3" style={{ width: '200px' }}>  
                    <Link className="nav-link" to="/">Home</Link>  
                    <Link className="nav-link" to="/messages">View Messages</Link>  
                    <Link className="nav-link" to="/register">Register</Link>  
                    <Link className="nav-link" to="/login">Login</Link>  {/* Added Login link */}  
                    <Link className="nav-link" to="/announcements">Announcements</Link>  
                </nav>  
                <main className="flex-fill p-3">  
                    <Routes>  
                        <Route path="/" element={<Home />} />  
                        <Route path="/messages" element={<MessagesList />} />  
                        <Route path="/register" element={<Register />} />  
                        <Route path="/login" element={<Login />} />  {/* Added Login route */}  
                        <Route path="/announcements" element={<Announcements />} />  
                    </Routes>  
                </main>  
            </div>  
            <footer className="bg-light text-center p-3 mt-auto">  
                <p>© 2024 Parent-Teacher Communication App. All rights reserved.</p>  
            </footer>  
        </div>  
    );  
};  

const Home = () => {  
    return (  
        <main>  
            <section className="hero">  
                <div className="container">  
                    <div className="row">  
                        <div className="col-md-6">  
                            <h2>Welcome to the Parent-Teacher Communication App!</h2>  
                            <p>This platform facilitates effective communication between parents and teachers.</p>  
                            <Link to="/register" className="btn btn-primary">Sign Up</Link>  
                        </div>  
                        <div className="col-md-6">  
                            <img src="/frontend/build/static/images.Didy.jpg" alt="Hero Image" className="img-fluid" />  
                        </div>  
                    </div>  
                </div>  
            </section>  
            <section className="features">  
                <div className="container">  
                    <h2 className="text-center my-4">Features of Our App</h2>  
                    <div className="row">  
                        <div className="col-md-4">  
                            <div className="card">  
                                <div className="card-body">  
                                    <h5 className="card-title">Secure Messaging</h5>  
                                    <p className="card-text">Communicate securely with teachers and parents in real-time.</p>  
                                </div>  
                            </div>  
                        </div>  
                        <div className="col-md-4">  
                            <div className="card">  
                                <div className="card-body">  
                                    <h5 className="card-title">Announcement Board</h5>  
                                    <p className="card-text">Stay updated with the latest announcements from the school.</p>  
                                </div>  
                            </div>  
                        </div>  
                        <div className="col-md-4">  
                            <div className="card">  
                                <div className="card-body">  
                                    <h5 className="card-title">User Profiles</h5>  
                                    <p className="card-text">Manage your profile and customize your experience.</p>  
                                </div>  
                            </div>  
                        </div>  
                    </div>  
                </div>  
            </section>  
        </main>  
    );  
};  

const Announcements = () => {  
    return (  
        <div className="container mt-4">  
            <h2>Announcements</h2>  
            <p>Stay tuned for the latest updates and events in our school community.</p>  
            <ul>  
                <li>  
                    <strong>Upcoming Event:</strong> Parent-Teacher Conference on February 15, 2025.  
                    <p>Join us for discussions about your child's progress.</p>  
                </li>  
                <li>  
                    <strong>School Closure:</strong> The school will be closed for staff training on January 20, 2025.  
                </li>  
            </ul>  
        </div>  
    );  
};  

export default App;
import { React } from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SubmitAssignment from './pages/submitAssignment.js';
import './App.css';
import Chat from './pages/chat.js';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<SubmitAssignment />}></Route>
        <Route path='/chat' element={<Chat />}></Route>
      </Routes>
    </Router>
    );
}

export default App;

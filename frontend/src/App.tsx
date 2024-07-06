import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';

function App() {
  return (
    <BrowserRouter>
      <Header />
      <div className="main"></div>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
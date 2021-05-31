import Header from './components/Header'
import SearchBar from './components/SearchBar'
import Hints from './components/Hints'
import AuthorsInputForm from './components/AuthorsInputForm'
import DocumentsInputForm from './components/DocumentsInputForm'
import Log from './components/Log'
import Downloads from './components/Downloads'
import Footer from './components/Footer'
import AuthorLog from './components/AuthorLog'

import { useState, useEffect } from 'react' 
import { BrowserRouter as Router, Route } from 'react-router-dom'

function App() {

  const [full_authors, setFAuthors] = useState([])
  const [authors, setAuthors] = useState([])
  const [log, setLog] = useState([])

  useEffect(() => {

    const getAuthors = async() => {
      const authorsFromServer = await fetchAuthors(false)
      console.log(authorsFromServer)
      setAuthors(authorsFromServer)
    }

    const getFAuthors = async() => {
      const authorsFromServer = await fetchAuthors(true)
      setFAuthors(authorsFromServer)
    }

    const getLog = async() => {
      const LogFromServer = await fetchLog()
      console.log(LogFromServer)
      setLog(LogFromServer)
    }

    getAuthors()
    getLog()
    getFAuthors()
  }, [])

  //Fetch Authors
  const fetchAuthors = async (full) => {
    const res = await fetch("http://127.0.0.1:5000/api/authors?full=" + full.toString())
    const data = await res.json()

    return data
  }

  const fetchLog = async () => {
    const res = await fetch("http://127.0.0.1:5000/api/log")
    const data = await res.json()

    return data
  }

  return (
    <Router>
    <div className="container">
      <Header/>
      <Route path='/' exact render={(props) => (
        <>
          <div id="cover">
            <img src="assets/cover.png" alt="cover"></img>
          </div>
        </>
      )} />
      <Route path='/start' exact render={(props) => (
        <>
          <SearchBar authors={authors.authors} FAuthors={full_authors.authors}/>
        </>
      )} />
      <Route path='/authors' exact render={(props) => (
        <>
          <AuthorLog authors={authors.authors}/>
        </>
      )} />
      <Route path='/documents' exact render={(props) => (
        <>
          <DocumentsInputForm />
        </>
      )} />
      <Route path='/log' exact render={(props) => (
        <>
          <Log logs={log.entries}/>
        </>
      )} />
      <Route path='/download' exact render={(props) => (
        <>
          <Downloads />
        </>
      )} />
      <Footer />
    </div>
    </Router>
  );
}

export default App;

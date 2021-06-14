import { useState } from 'react'
import { useHistory } from 'react-router-dom';
import { Button, FormControl } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

const Search = () => {
  const history = useHistory()
  const [ticker, setTicker ] = useState('')
  return <div style={{marginTop: 100, display: 'flex', flexDirection: 'column'}}>
  <h2>
    Анализ тональности текста новостных заголовков 
  </h2>
  <div  style={{display: 'flex'}}>
    <FormControl aria-label="First name" />
    <Button variant="dark" onClick={() => {history.push(`/result/${ticker}`)}}>найти</Button>
  </div>
  
  </div>
  
}

export default Search
import { useState, useEffect } from 'react'
import { useHistory } from 'react-router-dom';
import { Button,  ButtonGroup } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

const Search = () => {
  const history = useHistory()
  
  const [period, setPeriod ] = useState(1)

  useEffect(() => {
    console.log(history.location.pathname)
  },[])
  return <div style={{marginTop: 100, display: 'flex', flexDirection: 'column'}}>
  <h2>
    Период анализа 
  </h2>
  <ButtonGroup className="mb-2">
    <Button variant={`${period === 0 ? 'dark' : 'outline-dark'}`} onClick={() => {setPeriod(0)}}>3 дня</Button>
    <Button variant={`${period === 1 ? 'dark' : 'outline-dark'}`} onClick={() => {setPeriod(1)}}>5 дней</Button>
    <Button variant={`${period === 2 ? 'dark' : 'outline-dark'}`} onClick={() => {setPeriod(2)}}>Неделя</Button>
    <Button variant={`${period === 3 ? 'dark' : 'outline-dark'}`} onClick={() => {setPeriod(3)}}>2 недели</Button>
  </ButtonGroup>
  <div  style={{display: 'flex'}}>
    {/* <Button variant="outline-dark" onClick={() => {history.push(`/result/${ticker}`)}}>найти</Button> */}
  </div>
  
  </div>
  
}

export default Search
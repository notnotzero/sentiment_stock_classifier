import { Navbar , Nav, Container } from 'react-bootstrap';

const NavComponent = () => {
 return  <Navbar bg="dark" variant="dark">
    <Container>
    <Navbar.Brand href="#home">Дипломная работа</Navbar.Brand>
    <Nav className="me-auto">
      <Nav.Link href="#home">О системе</Nav.Link>
      <Nav.Link href="#home">Контакты</Nav.Link>
    </Nav>
    </Container>
  </Navbar>
}

export default NavComponent
import { Link } from 'react-router-dom'

const footer = () => {
    return (
        <footer className='footer'>
            <p>Copyright &copy; Yousef Radwan 2021</p>
            <Link to = '/about'>About</Link>
        </footer>
    )
}

export default footer

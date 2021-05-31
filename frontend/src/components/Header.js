import PropTypes from 'prop-types'
import NavBar from './NavBar'


const Header = ({ title, icon }) => {

    return (
        <div id='header'>
            <div className='headerdiv'>
                <header className='header'>
                    <h1 id='title'>{title}</h1>
                    <img id = "icon" src = "assets/icon.png" alt="icon"></img>
                </header>
            </div>
            <NavBar />
        </div>
    )
}

Header.defaultProps = {
    title: 'Scop.io',
}

Header.propTypes = {
    title: PropTypes.string.isRequired
}

export default Header

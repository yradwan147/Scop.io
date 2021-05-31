import { Link } from 'react-router-dom'

const NavElement = ({ title, icon, path }) => {
    return (
        <Link to = {path}>
            <div className="navelement">
                <h3>{title}</h3>
                <img className="navicon" src={icon} alt="icon"></img>
            </div>
        </Link>
    )
}

export default NavElement

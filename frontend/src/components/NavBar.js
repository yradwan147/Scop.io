import NavElement from './NavElement'

const NavBar = () => {
    return (
        <div className='navbar'>
                <NavElement title="Start" icon="assets/start.png" path="/start"/>
                <NavElement title="Authors" icon="assets/authors.png" path="/authors"/>
                <NavElement title="Documents" icon="assets/documents.png" path="/documents"/>
                <NavElement title="Logger" icon="assets/log.png" path="/log"/>
                <NavElement title="Downloads" icon="assets/downloads.png" path="/download"/>
        </div>
    )
}

export default NavBar

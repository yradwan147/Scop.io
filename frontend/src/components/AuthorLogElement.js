import Author from './Author'
import { useState } from 'react' 

const AuthorLogElement = ({ author, name, documents, citations, h_index, coauthor1, coauthor2, coauthor3, flag }) => {

    const [Details, setDetails] = useState(false)

    const toDate = (timestamp)=>{
        const milliseconds = timestamp * 1000 
        const dateObject = new Date(milliseconds)
        const humanDateFormat = dateObject.toLocaleString()
        return humanDateFormat
    }

    return (
        <>
        <tr>
            {flag && <td>{toDate(author.timestamp)}</td>}
            <td><button className="authorButton" onClick={()=>{setDetails(!Details)}}>{name}</button></td>
            <td>{documents}</td>
            <td>{citations}</td>
            <td>{h_index}</td>
            <td>{coauthor1}</td>
            <td>{coauthor2}</td>
            <td>{coauthor3}</td>
            <td className="topicsCell">
                <ol>
                    <li>{author.topic1}</li>
                    <li>{author.topic2}</li>
                    <li>{author.topic3}</li>
                </ol>
            </td>
        </tr>
        {Details && <Author author={author}/>}
        </>
            

    )
}

export default AuthorLogElement

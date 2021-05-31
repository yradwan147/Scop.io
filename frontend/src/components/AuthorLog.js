import AuthorLogElement from "./AuthorLogElement"

const AuthorLog = ({ authors, flag }) => {
    return (
        <table>
            <tr id="tableheader">
                {flag && <th>Timestamp</th>}
                <th>Name</th>
                <th>Documents</th>
                <th>Citations</th>
                <th>h_index</th>
                <th>Coauthor 1</th>
                <th>Coauthor 2</th>
                <th>Coauthor 3</th>
                <th>Top Topics</th>
            </tr>
            {authors.map((author) => (<AuthorLogElement author={author} key={author.id} name={author.name} documents={author.documentsNumber} citations = {author.citationsNumber} h_index = {author.h_index} coauthor1 = {author.coauthor1} coauthor2 = {author.coauthor2} coauthor3 = {author.coauthor3} flag={flag}/>) )}
        </table>
    )
}

export default AuthorLog

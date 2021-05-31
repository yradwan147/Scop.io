const LogElement = ({ timestamp, request, response, status_code }) => {
    
    const toDate = (timestamp)=>{
        const milliseconds = timestamp * 1000 
        const dateObject = new Date(milliseconds)
        const humanDateFormat = dateObject.toLocaleString()
        return humanDateFormat
    }
    
    return (
        <tr>
            <th>{toDate(timestamp)}</th>
            <th>{request.slice(0,100)}</th>
            <th>{response.slice(0,100)}</th>
            <th>{status_code}</th>
        </tr>
    )
}

export default LogElement

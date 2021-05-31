import LogElement from './LogElement'

const Log = ({ logs }) => {
    return (
        <table>
            <tr id="tableheader">
                <th>Timestamp</th>
                <th>Request</th>
                <th>Response</th>
                <th>Status Code</th>
            </tr>
            {logs.map((log) => (<LogElement timestamp={log.timestamp} request={log.request} response = {log.response} status_code = {log.status_code} />) )}
        </table>
    )
}

export default Log

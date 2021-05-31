const Downloads = () => {

    const fetchAuthorsDownload = async () => {
        const res = await fetch("http://127.0.0.1:5000/api/downloads/authors")
        console.log(res)
        const data = await res.blob()
        console.log(data)
        
    
        return data
      }

    const onSubmit = (e)=> {
        e.preventDefault();
        fetchAuthorsDownload();

    }

    

    return (
        <div id="downloads">
            <div className="download">
                <img className="downloadicon" src="assets/authors.png" alt="download"></img>
                <h2 className="downloadTitle">Authors</h2>
                <div className="downloadButton">
                    <a className="downloadText" href='http://127.0.0.1:5000/api/downloads/authors' download>Download</a>
                </div>
            </div>
        </div>
    )
}

export default Downloads

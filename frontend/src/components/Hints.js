const Hints = () => {
    return (
        <div className="hints">
            <h2>Hints</h2>
            <h3>TOP commands:</h3>
            <ul className="hintslist">
                <li>
                    TOP <span className="hintvariable">number</span> TOPIC <span className="hintvariable">topic</span>
                    <span class="tooltiptext">Search for authors with selected topic in their top 3 topics</span>
                </li>
                <li>
                    TOP <span className="hintvariable">number</span> PUBLICATIONS
                    <span class="tooltiptext">Search for top authors according to number of documents</span>
                </li>
                <li>
                    TOP <span className="hintvariable">number</span> CITATIONS
                    <span class="tooltiptext">Search for top authors according to number of citations</span>
                </li>
                <li>
                    TOP <span className="hintvariable">number</span> H_INDEX
                    <span class="tooltiptext">Search for top authors according to h_index</span>
                </li>
                <li>
                    TOP <span className="hintvariable">number</span> PUBLICATIONSR <span className="hintvariable">startyear endyear (descending)</span>
                    <span class="tooltiptext">Search for top authors with publications in given range</span>
                </li>
                <li>
                    TOP <span className="hintvariable">number</span> CITATIONSR <span className="hintvariable">startyear endyear (descending)</span>
                    <span class="tooltiptext">Search for top authors with citations in given range</span>
                </li>
                <li>
                    TOP <span className="hintvariable">number</span> COAUTHOR <span className="hintvariable">coauthor</span>
                    <span class="tooltiptext">Search for top authors who've coauthored with this person</span>
                </li>
            </ul>
            <h3>SEARCH commands:</h3>
            <ul>
                <li className="hintslist">
                    SEARCH NAME <span className="hintvariable">name</span>
                    <span class="tooltiptext">Search for author and all of his iterations in the database</span>
                </li>
            </ul>
            <h3>CLEAR<span class="tooltiptext">Clear console</span></h3>
        </div>
    )
}

export default Hints

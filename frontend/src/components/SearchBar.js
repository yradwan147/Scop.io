import ReactDOM from 'react-dom'
import AuthorLog from './AuthorLog'
import Hints from './Hints'

const SearchBar = ({ authors, FAuthors }) => {

    //console.log(eval(item['publications'])[0]['Authors'])
    // let uni =item['university'].replace(/'/g,'"');
    // let affiliations = JSON.parse(uni)

    const Affiliate = (uni, year) => {
        let output = []
        authors.forEach((item,index)=>{
            let affiliations = JSON.parse(uni)
            affiliations.keys().forEach((item1,index)=>{
                if (item1.search(uni) !== -1){
                    if (affiliations[item1].includes(year.parseInt())){
                        output.push(item)
                    }
                }
            })
            })

        return output;
    }

    const searchJournal= (journal, number) =>{
        authors.forEach((item,index)=>{
            let publications = eval(item['publications'])
            let value = 0;
            publications.forEach((item,index)=> {
                if (item['Journal'].search(journal) !== -1){
                    value+=1;
                }
            })
            item['value'] = value;
            })
        let sortedJournal = authors.sort(function(a,b) {
            return b.value - a.value
        });

        return sortedJournal.slice(0,number)
    }

    const searchCoauthor = (coauthor, number) => {
        let value;
        let dataset = authors.slice()
        console.log(dataset.length)
        dataset.forEach((item,index)=>{
            if (item['coauthor1'].toLowerCase().search(coauthor) !== -1){
                value = parseInt(item['coauthor1'].split(' ').slice(-1).join(''));
            }else if (item['coauthor2'].toLowerCase().search(coauthor) !== -1){
                value = parseInt(item['coauthor2'].split(' ').slice(-1).join(''));
            }else if (item['coauthor3'].toLowerCase().search(coauthor) !== -1){
                value = parseInt(item['coauthor3'].split(' ').slice(-1).join(''));
            }else{
                value = 0;
            }
            item['value'] = value;
            })
        let sortedCoauthors = dataset.sort(function(a,b) {
            return b.value - a.value
        });
        for (let i = 0; i < sortedCoauthors.length; i++){
            if (sortedCoauthors[i]['value'] == 0){
                sortedCoauthors = sortedCoauthors.slice(0,i)
            }
        }

        return sortedCoauthors.slice(0,number)
    }
    
    const searchName = (name) => {
        let output = []
        FAuthors.forEach((item, index)=>{
            if (item['name'].toLowerCase().search(name) !== -1){
                output.push(item)
            }
        })
        let sortedTime = output.sort(function(a,b) {
            return b.timestamp - a.timestamp
        });
        return sortedTime
    }

    const searchTopic = (topic, number) => {
        let output = []
        authors.forEach((item,index)=>{
            console.log(item['topic1'])
            if (item['topic1'].toLowerCase().search(topic) !== -1 || item['topic2'].toLowerCase().search(topic) !== -1 || item['topic3'].toLowerCase().search(topic) !== -1){
                output.push(item)
            }
        })
        return output.slice(0,number);
    }

    const searchPublications = (number)=> {
        let sortedPublications = authors.sort(function(a,b) {
            return b.documentsNumber - a.documentsNumber
        });
        return sortedPublications.slice(0,number)
    }

    const searchH_index = (number)=> {
        let sortedH_index = authors.sort(function(a,b) {
            return b.h_index - a.h_index
        });
        return sortedH_index.slice(0,number)
    }

    const searchCitations = (number)=> {
        let sortedCitations = authors.sort(function(a,b) {
            return b.citationsNumber - a.citationsNumber
        });
        return sortedCitations.slice(0,number)
    }

    const searchPublicationsR = (start,end,number)=> {
        authors.forEach((item,index)=>{
            let value = (JSON.parse(item['publicationsStats'].replace(/'/g, '"'))).slice(2021-start, 2021-end).reduce((a, b) => a + b, 0);
            item['value'] = value;
            })
        let sortedPublicationsR = authors.sort(function(a,b) {
            return b.value - a.value
        });

        return sortedPublicationsR.slice(0,number)
    }

    const searchCitationsR = (start,end,number)=> {
        authors.forEach((item,index)=>{
            let value = (JSON.parse(item['citationsStats'].replace(/'/g, '"'))).slice(2021-start, 2021-end).reduce((a, b) => a + b, 0);
            item['value'] = value;
            })
        let sortedCitationsR = authors.sort(function(a,b) {
            return b.value - a.value
        });

        return sortedCitationsR.slice(0,number)
    }

    const searchUniversities = (uni, number) => {
        let output = []
        authors.forEach((item,index) => {
            console.log(item['university'])
            if (item['university'].toLowerCase().search(uni) !== -1){
                output.push(item)
            }
        })
        let sortedOH_index = output.sort(function(a,b) {
            return b.h_index - a.h_index
        });
        return sortedOH_index.slice(0,number)
    }

    const onChange = (e) => {
        e.preventDefault()

        let value = e.target.value
        console.log(value)
        let index1 = value.toLowerCase().indexOf('top')
        let index2 = value.toLowerCase().indexOf('search')
        let index3 = value.toLowerCase().indexOf('clear')
        let index4 = value.toLowerCase().indexOf('affiliate')
        console.log(index1, index2)
        if (index1 !== -1) {
            document.getElementById('consoletyper').innerHTML= "<span class='command1'><p>TOP</p></span>" + "<p>"+ value.slice(index1+3, ) + "</p>"
        }else if (index2 !== -1) {
            document.getElementById('consoletyper').innerHTML= "<span class='command2'><p>SEARCH</p></span>" + "<p>"+ value.slice(index2+6, ) + "</p>"
        }else if (index3 !== -1) {
            document.getElementById('consoletyper').innerHTML= "<span class='command3'><p>CLEAR</p></span>" + "<p>"+ value.slice(index3+5, ) + "</p>"
        }else if (index4 !== -1) {
            document.getElementById('consoletyper').innerHTML= "<span class='command4'><p>CLEAR</p></span>" + "<p>"+ value.slice(index4+9, ) + "</p>"
        }else{
            document.getElementById('consoletyper').innerHTML = ""
        }

    }

    const onSubmit = (e) => {
        e.preventDefault();
        let commandHTML = document.getElementById('consoletyper').innerHTML;
        let startingindex = commandHTML.search('</span>') + 11;
        let command_content = commandHTML.slice(startingindex, -4)
        let command = commandHTML.slice(commandHTML.search("><p>") + 4, commandHTML.search("</p></span>"))
        console.log(command, command_content)
        if (command.toLowerCase() === "top"){
            console.log('here')
            let command_elements = command_content.split(' ')
            let number = command_elements[0];
            for (let i = 0; i < command_elements.length; i++){
                console.log(command_elements[i].toLowerCase())
                if (command_elements[i].toLowerCase() === 'topic'){
                    let selectedTopic = command_elements.slice(i+1, ).join(' ');
                    let authorsr = searchTopic(selectedTopic, number);
                    console.log(authorsr)
                    ReactDOM.render(
                        <AuthorLog authors={authorsr} />
                        , document.getElementById('resultwindow'));
                }else if (command_elements[i].toLowerCase() === 'publications'){
                    let authorsr = searchPublications(number);
                    ReactDOM.render(
                        <AuthorLog authors={authorsr} />
                        , document.getElementById('resultwindow'));
                }else if (command_elements[i].toLowerCase() === 'h_index'){
                    let authorsr = searchH_index(number);
                    ReactDOM.render(
                        <AuthorLog authors={authorsr} />
                        , document.getElementById('resultwindow'));
                }else if (command_elements[i].toLowerCase() === 'citations'){
                    let authorsr = searchCitations(number);
                    ReactDOM.render(
                        <AuthorLog authors={authorsr} />
                        , document.getElementById('resultwindow'));
                }else if (command_elements[i].toLowerCase() === 'publicationsr'){
                    let selectedRangeStart = command_elements[i+1];
                    let selectedRangeEnd = command_elements[i+2];
                    let authorsr = searchPublicationsR(selectedRangeStart, selectedRangeEnd, number);
                    console.log(authorsr ,selectedRangeEnd, selectedRangeStart)
                    ReactDOM.render(
                        <AuthorLog authors={authorsr} />
                        , document.getElementById('resultwindow'));
                }else if (command_elements[i].toLowerCase() === 'citationsr'){
                    let selectedRangeStart = command_elements[i+1];
                    let selectedRangeEnd = command_elements[i+2];
                    let authorsr = searchCitationsR(selectedRangeStart, selectedRangeEnd, number);
                    ReactDOM.render(
                        <AuthorLog authors={authorsr} />
                        , document.getElementById('resultwindow'));
                }else if (command_elements[i].toLowerCase() === 'university'){
                    let selectedUni = command_elements.slice(i+1, ).join(' ');
                    let authorsr = searchUniversities(selectedUni, number);
                    ReactDOM.render(
                        <AuthorLog authors={authorsr} />
                        , document.getElementById('resultwindow'));
                }else if (command_elements[i].toLowerCase() === 'coauthor'){
                    let selectedCoauthor = command_elements.slice(i+1, ).join(' ');
                    let authorsr = searchCoauthor(selectedCoauthor, number);
                    console.log(authorsr)
                    ReactDOM.render(
                        <AuthorLog authors={authorsr} />
                        , document.getElementById('resultwindow'));
                }else if (command_elements[i].toLowerCase() === 'journal'){
                    let selectedjournal = command_elements.slice(i+1, ).join(' ');
                    let authorsr = searchJournal(selectedjournal, number);
                    console.log(authorsr)
                    ReactDOM.render(
                        <AuthorLog authors={authorsr} />
                        , document.getElementById('resultwindow'));
                }
            }
        }else if (command.toLowerCase() === "clear"){
            console.log('here2')
            ReactDOM.unmountComponentAtNode(document.getElementById('resultwindow'))
        }else if (command.toLowerCase() === "affiliate"){
            let command_elements = command_content.split(' ')
            let uni = command_elements[0];
            let year = command_elements[1];
            let authorsr = Affiliate(uni, year);
            ReactDOM.render(
                <AuthorLog authors={authorsr} />
                , document.getElementById('resultwindow'));

        }else if (command.toLowerCase() === "search"){
            let command_elements = command_content.split(' ')
            for (let i = 0; i < command_elements.length; i++){
                console.log(command_elements[i].toLowerCase())
                if (command_elements[i].toLowerCase() === 'name'){
                    let selectedName = command_elements.slice(i+1, ).join(' ');
                    let authorsr = searchName(selectedName);
                    ReactDOM.render(
                        <AuthorLog authors={authorsr} flag={true}/>
                        , document.getElementById('resultwindow'));
                }else if (command_elements[i].toLowerCase() === 'university'){
                    //TODO
                }

            }
        }
    }

    return (
        <div className='searchbardiv'>
            <form className='searchbar' onSubmit = {onSubmit}>
                <input type="text" id="console" name="console" onChange={onChange} ></input>
            </form>
            <Hints />
            <div id='consoletyper' className='consoletyper'></div>
            <div id='resultwindow'></div>
        </div>
    )
}

export default SearchBar

import AnyChart from 'anychart-react'
import anychart from 'anychart'
import lodash from 'lodash'

const Author = ({ author }) => {

    const lister = (list_string) => {
        console.log(list_string)
        let list = JSON.parse(list_string.replace(/'/g, '"'))
        let output = []
        lodash.range(2021, 1969,-1).forEach((item, index)=>{output.push([item, list[index]])})
        console.log(output)
        return output
    }

    const coauthor_parse = (coauthor) => {
        let coauthor_elements = coauthor.split(' ')
        console.log(coauthor_elements)
        let output = [(coauthor_elements.slice(0,-1)).join(' '), parseInt(coauthor_elements.slice(-1).join())]
        return output
    }

    let stage = anychart.graphics.create()
    let data1 = lister(author.citationsStats)
    let data2 = lister(author.publicationsStats)
    let data4 = [coauthor_parse(author.coauthor1), coauthor_parse(author.coauthor2), coauthor_parse(author.coauthor3), coauthor_parse(author.coauthor4), coauthor_parse(author.coauthor5), coauthor_parse(author.coauthor6), coauthor_parse(author.coauthor7), coauthor_parse(author.coauthor8)]
    console.log(data4)
    let chart1 = anychart.line(data1)
    var title1 = chart1.title();
    title1.text("Citations");
    title1.enabled(true);
    let chart2 = anychart.column(data2);
    var title2 = chart2.title();
    title2.text("Publications");
    title2.enabled(true);
    let chart3 = anychart.pie([{x:'Article', value:author.articleNumber}, {x:'Conference', value:author.conferenceNumber}, {x:'Book Chapter', value:author.bookchapterNumber},
    {x:'Editorial', value:author.editorialNumber}, {x:'Review', value:author.reviewNumber}, {x:'Book', value:author.bookNumber}, {x:'Erratum', value:author.erratumNumber}, {x:'Letter', value:author.letterNumber}])
    var title3 = chart3.title();
    title3.text("Document Type Distribution");
    title3.enabled(true);
    let chart4 = anychart.column(data4)
    var title4 = chart4.title();
    title4.text("Coauthors");
    title4.enabled(true);
    chart1.bounds(0,0,'25%', '100%');
    chart2.bounds('25%',0, '25%', '100%');
    chart3.bounds('50%',0, '25%', '100%');
    chart4.bounds('75%',0, '25%', '100%');
//
    return (
        <td colSpan="9" className="authorDetails">
            <AnyChart 
            instance={stage}
            width={'100%'}
            height={400}
            charts={[chart1, chart2, chart3, chart4]}
            />
        </td>
    )
}

export default Author

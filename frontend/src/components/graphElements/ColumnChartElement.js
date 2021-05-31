import AnyChart from 'anychart-react'

const ColumnChartElement = ({ data, title, width, height }) => {

    const complexSettings = {
        width: {width},
        height: {height},
        type: 'column',
        data: {data},
        //"P1,5\nP2,3\nP3,6\nP4,4"
        title: {title},
        yAxis: [1, {
          orientation: 'right',
          enabled: true,
          labels: {
            format: '{%Value}{decimalPoint:\\,}',
            fontColor: 'red'
          }
        }],
        legend: {
          background: 'lightgreen 0.4',
          padding: 0
        },
        lineMarker: {
          value: 4.5
        }
      };

    return (
        <div className='columnDiv'>
          <AnyChart
            {...complexSettings}
        />  
        </div>
    )
}

export default ColumnChartElement

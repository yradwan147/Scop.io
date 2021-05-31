import AnyChart from 'anychart-react'

const LineChartElement = ({ data, title, width, height }) => {
    return (
        <div className="lineDiv">
            <AnyChart
                width={width}
                height={height}
                type="line"
                data={data}
                title={title}
            />
        </div>
    )
}

export default LineChartElement

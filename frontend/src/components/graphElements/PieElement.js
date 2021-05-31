import AnyChart from 'anychart-react'

const PieElement = ({ data, title, width, height }) => {
    return (
        <div className='pieDiv'>
            <AnyChart
                width={width}
                height={height}
                type="pie"
                data={data}
                position={0,100,0,100}
                //[1, 2, 3, 4]
                title={title}
            />
        </div>
    )
}

export default PieElement

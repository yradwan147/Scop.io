import AnyChart from 'anychart-react'

// let data = anychart.data.set([
//   {'id': 'AU.WA', 'value': 300},
//   {'id': 'AU.JB', 'value': 230},
//   {'id': 'AU.NS', 'value': 240},
//   {'id': 'AU.VI', 'value': 275},
//   {'id': 'AU.NT', 'value': 130},
//   {'id': 'AU.TS', 'value': 190},
//   {'id': 'AU.CT', 'value': 100},
//   {'id': 'AU.SA', 'value': 305},
//   {'id': 'AU.QL', 'value': 190}
// ]);

// please do not forget to include the map to your html file (<head> section)
// <script src="path/to/node_modules/anychart/dist/geodata/countries/australia/australia.js"></script>

const ChloropethMapElement = ({ data, geoData, title, width, height }) => {
return (
    <div className='choloropethDiv'>
        <AnyChart
            width={width}
            height={height}
            type="choropleth"
            data={data}
            title={title}
            geoData={geoData}
            //"anychart.maps.australia"
        />
    </div>
    )
}
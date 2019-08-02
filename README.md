### Create hexagon indexes
---
*This code will produce set of hexagon indexes for given polygon, which tiled the entire polygon area. We have used the following 3rd party packages.  [h3-js](https://github.com/uber/h3-js) for get a hexagon index for given lat|lon value and [geojson2h3](https://github.com/uber/geojson2h3) for get set of hexagon index for given polygon.*

import **geojson2h3** library
```const geojson2h3 = require('geojson2h3')```

getting set of hexagons, which are fill the given polygon
```const Hexagons = geojson2h3.featureToH3Set(DATA, RESOLUTION)```

result will be,




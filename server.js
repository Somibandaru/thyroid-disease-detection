const express = require('express');
const fetch = require('node-fetch');
const app = express();
const port = 3000;

app.use(express.static('public'));

app.get('/getThyroidHospitals', async (req, res) => {
    const lat = req.query.lat;
    const lon = req.query.lon;

    // Overpass API URL for the query (MapQuest Overpass API)
    const overpassApiUrl = `https://overpass.kumi.systems/api/interpreter?data=node(around:90000,${lat},${lon})[amenity=hospital][healthcare=speciality][speciality=thyroid](${lat - 0.1},${lon - 0.1},${lat + 0.1},${lon + 0.1});out;`;

    try {
        const response = await fetch(overpassApiUrl);
        const data = await response.json();
        res.json(data);
    } catch (error) {
        console.error('Error fetching data:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});

import express from 'express';
import mongoose from 'mongoose';

const app = express();
const port = 3000;

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/marathon', { useNewUrlParser: true, useUnifiedTopology: true });

// Define the AthleteLocation model
const athleteLocationSchema = new mongoose.Schema({
    beaconPosition: { type: Number, min: 1, max: 5, required: true },
    location: {
        type: { type: String, default: 'Point' },
        coordinates: [Number]
    },
    eventTimestamp: { type: Date, required: true },
    athleteId: { type: String, required: true }
});

athleteLocationSchema.index({ location: '2dsphere' });

const AthleteLocation = mongoose.model('AthleteLocation', athleteLocationSchema);

// Use express.json() middleware to parse JSON bodies
app.use(express.json());

// POST endpoint to store athlete locations
app.post('/locations', async (req, res) => {
    try {
        const { beaconPosition, latitude, longitude, eventTimestamp, athleteId } = req.body;
        if (!beaconPosition || !latitude || !longitude || !eventTimestamp || !athleteId) {
            return res.status(400).json({ message: 'All fields are required' });
        }

        const location = {
            type: 'Point',
            coordinates: [longitude, latitude]
        };

        const athleteLocation = new AthleteLocation({
            beaconPosition,
            location,
            eventTimestamp,
            athleteId
        });

        await athleteLocation.save();

        res.status(201).json({ message: 'Athlete location saved successfully' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});

if (require.main === module) {
    app.listen(port, () => {
        console.log(`Server is running on port ${port}`);
    });
}

export default app;

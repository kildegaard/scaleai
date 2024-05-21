import mongoose from 'mongoose';
import { MongoMemoryServer } from 'mongodb-memory-server';
import request from 'supertest';
import { expect } from 'chai';
import app from '../app.mjs';  // Ensure this path is correct

let mongoServer;

before(async () => {
    mongoServer = await MongoMemoryServer.create();
    const uri = mongoServer.getUri();

    await mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true });
});

after(async () => {
    await mongoose.disconnect();
    await mongoServer.stop();
});

describe('POST /locations', () => {
    it('should save athlete location with valid input', async () => {
        const response = await request(app)
            .post('/locations')
            .send({
                beaconPosition: 3,
                latitude: 40.7128,
                longitude: -74.0060,
                eventTimestamp: new Date().toISOString(),
                athleteId: 'athlete123'
            });

        expect(response.status).to.equal(201);
        expect(response.body.message).to.equal('Athlete location saved successfully');
    });

    it('should return 400 if any field is missing', async () => {
        const response = await request(app)
            .post('/locations')
            .send({
                latitude: 40.7128,
                longitude: -74.0060,
                eventTimestamp: new Date().toISOString(),
                athleteId: 'athlete123'
            });

        expect(response.status).to.equal(400);
        expect(response.body.message).to.equal('All fields are required');
    });

    it('should return 400 if beaconPosition is out of range', async () => {
        const response = await request(app)
            .post('/locations')
            .send({
                beaconPosition: 6,
                latitude: 40.7128,
                longitude: -74.0060,
                eventTimestamp: new Date().toISOString(),
                athleteId: 'athlete123'
            });

        expect(response.status).to.equal(400);
    });

    it('should return 500 for invalid data types', async () => {
        const response = await request(app)
            .post('/locations')
            .send({
                beaconPosition: 'invalid',
                latitude: 'invalid',
                longitude: 'invalid',
                eventTimestamp: 'invalid',
                athleteId: 123
            });

        expect(response.status).to.equal(500);
    });
});

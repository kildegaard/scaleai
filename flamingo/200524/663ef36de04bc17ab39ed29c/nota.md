# Prompt 1

I'm building an application for a local marathon. We'll have beacons during the track, we can't make sure they're evenly spread because it's a race within the city. Every time an athlete passes through a beacon, we'll send the beacon's position, latitude, longitude, event_timestamp, and athlete's ID to a server, so we can keep track of the athlete's location during the race. Implement this as an Express server with a POST endpoint to store into MongoDB, using its geospatial features. All fields are required. For the beacon position, it's an integer from 1 to 5.

Now create a new endpoint to return the first 5 athletes who finished the marathon in less time. Please also include a beacon-to-beacon performance comparison for each one of them.

Create a new endpoint to return the average speed of all athletes for each step, and also return who was the fastest in each step.



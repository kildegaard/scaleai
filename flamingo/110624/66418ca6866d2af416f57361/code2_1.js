class Department {
    constructor(name, staffCount) {
        this.name = name;
        this.staffCount = staffCount;
    }
}

class Floor {
    constructor(seats) {
        this.seats = seats;
        this.departments = [];
        this.occupiedSeats = 0;
    }

    addDepartment(department) {
        this.departments.push(department);
        this.occupiedSeats += department.staffCount;
    }

    getOccupancy() {
        return this.occupiedSeats / this.seats;
    }
}

class OfficeBuilding {
    constructor(floors, seatsPerFloor) {
        this.floors = Array(floors).fill(0).map(() => new Floor(seatsPerFloor));
    }

    addDepartment(department) {
        // Sort floors by occupancy
        this.floors.sort((a, b) => a.getOccupancy() - b.getOccupancy());

        // Try to add the department to the floor with the lowest occupancy
        for (let i = 0; i < this.floors.length; i++) {
            const floor = this.floors[i];
            if (floor.getOccupancy() < 0.65 && floor.departments.length < 3) {
                floor.addDepartment(department);
                return;
            }
        }

        // If no floor has enough space, add the department to the floor with the lowest occupancy
        this.floors[0].addDepartment(department);
    }
}

// Example usage
const staffCount = 100;
const floors = 5;
const seatsPerFloor = 50;
const departments = [
    new Department('Sales', 20),
    new Department('Marketing', 15),
    new Department('IT', 10),
    new Department('HR', 5),
    new Department('Finance', 20),
    new Department('Operations', 30)
];

const officeBuilding = new OfficeBuilding(floors, seatsPerFloor);

departments.forEach(department => {
    // Split the department into two groups: 2/3 and 1/3
    const twoThirds = Math.ceil(department.staffCount * 2 / 3);
    const oneThird = department.staffCount - twoThirds;

    // Add the 2/3 group to the office building
    officeBuilding.addDepartment(new Department(department.name, twoThirds));

    // Add the 1/3 group to the office building
    officeBuilding.addDepartment(new Department(department.name, oneThird));
});

// Print the occupancy of each floor
officeBuilding.floors.forEach((floor, index) => {
    console.log(`Floor ${index + 1}: ${floor.getOccupancy() * 100}% occupied`);
    console.log(`Departments: ${floor.departments.map(department => department.name).join(', ')}`);
});
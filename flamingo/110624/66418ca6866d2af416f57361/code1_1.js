function allocateSeats(staffCount, floorCount, seatsPerFloor) {
    // Calculate the maximum number of staff per floor
    const maxStaffPerFloor = Math.floor(seatsPerFloor * 0.65);

    // Initialize an array to hold the department allocations
    const departmentAllocations = new Array(floorCount).fill(0).map(() => []);

    // Initialize an array to hold the staff counts per floor
    const staffCounts = new Array(floorCount).fill(0);

    // Loop through each department
    for (let department = 0; department < staffCount; department++) {
        // Calculate the number of staff in this department
        const departmentStaffCount = Math.floor(staffCount / (department + 1));

        // Calculate the number of staff to allocate to the primary floor
        const primaryFloorStaffCount = Math.floor(departmentStaffCount * 2 / 3);

        // Find a floor that can accommodate the primary staff count
        let primaryFloor = findAvailableFloor(departmentAllocations, staffCounts, maxStaffPerFloor, primaryFloorStaffCount);

        // Add the primary staff count to the primary floor
        console.log(typeof departmentAllocations[primaryFloor])
        //departmentAllocations[primaryFloor].push(department);
        staffCounts[primaryFloor] += primaryFloorStaffCount;

        // Calculate the number of staff to allocate to the secondary floor
        const secondaryFloorStaffCount = departmentStaffCount - primaryFloorStaffCount;

        // Find a floor that can accommodate the secondary staff count
        let secondaryFloor = findAvailableFloor(departmentAllocations, staffCounts, maxStaffPerFloor, secondaryFloorStaffCount, primaryFloor);

        // Add the secondary staff count to the secondary floor
        
        //departmentAllocations[secondaryFloor].push(department);
        staffCounts[secondaryFloor] += secondaryFloorStaffCount;
    }

    // Return the department allocations
    return departmentAllocations;
}

function findAvailableFloor(departmentAllocations, staffCounts, maxStaffPerFloor, staffCount, avoidFloor = -1) {
    // Loop through each floor
    for (let floor = 0; floor < departmentAllocations.length; floor++) {
        // Skip the avoid floor
        if (floor === avoidFloor) {
            continue;
        }

        // Check if the floor can accommodate the staff count
        if (staffCounts[floor] + staffCount <= maxStaffPerFloor) {
            // Check if the floor has at least three departments
            if (departmentAllocations[floor].length >= 3 || (departmentAllocations[floor].length + 1) >= 3) {
                return floor;
            }
        }
    }

    // If no floor is found, return -1
    return -1;
}

// Test the function
const staffCount = 100;
const floorCount = 5;
const seatsPerFloor = 100;

const departmentAllocations = allocateSeats(staffCount, floorCount, seatsPerFloor);
console.log(departmentAllocations);
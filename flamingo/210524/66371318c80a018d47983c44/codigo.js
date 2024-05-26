function addStudentToTeacher(student, teacherName, teachers) {
    // Find the teacher by name
    const teacher = teachers.find(t => `${t.firstName} ${t.lastName}` === teacherName);

    if (teacher) {
        // Add the student to the teacher's students array
        teacher.students.push(student);
    } else {
        console.log(`Teacher ${teacherName} not found.`);
    }
}

// Example usage:
const teachers = [
    {
        firstName: 'John',
        lastName: 'Doe',
        roomNumber: 101,
        students: []
    },
    {
        firstName: 'Jane',
        lastName: 'Smith',
        roomNumber: 202,
        students: []
    }
];

const newStudent = {
    firstName: 'Bobby',
    lastName: 'Johnson',
    age: 12,
    parentName: 'Mrs. Johnson'
};

addStudentToTeacher(newStudent, 'John Doe', teachers);

console.log(teachers);
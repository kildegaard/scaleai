const fs = require("fs");
const chalk = require("chalk");

const addNote = (title, body) => {
    const notes = loadNotes();
    const duplicateNote = notes.find((note) => note.title === title);

    if (!duplicateNote) {
        notes.push({
            title: title,
            body: body,
        });
        saveNots(notes);
        console.log(chalk.green.inverse("New Note Added!"));
    } else {
        console.log(chalk.red.inverse("Note Already Exists!"));
    }
};

const saveNots = (notes) => {
    const dataJson = JSON.stringify(notes);
    fs.writeFileSync("notes.json", dataJson);
};

const loadNotes = () => {
    try {
        const dataBuffer = fs.readFileSync("notes.json");
        const dataJson = dataBuffer.toString();
        return JSON.parse(dataJson);
    } catch (e) {
        return [];
    }
};

const removeNotes = (title) => {
    const notes = loadNotes();
    const fondNotes = notes.filter((note) => note.title !== title);

    if (notes.length > fondNotes.length) {
        console.log(chalk.green.inverse("Note Removed!"));
        saveNots(fondNotes);
    } else {
        console.log(chalk.red.inverse("Note Not Found!"));
    }
};

const listNotes = () => {
    const notes = loadNotes();
    console.log(chalk.green("Your Notes!"));
    notes.forEach((note) => {
        console.log(note.title);
    });
};

const readNote = (title) => {
    const notes = loadNotes();
    const findNote = notes.find((note) => note.title === title);

    if (findNote) {
        console.log(chalk.gray.inverse(findNote.title));
        console.log(findNote.body);
    } else {
        console.log(chalk.red("Error!"));
    }
};

module.exports = {
    addNote: addNote,
    removeNotes: removeNotes,
    listNotes: listNotes,
    readNote: readNote,
};
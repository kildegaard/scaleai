const notes = require("./notes");
const chalk = require("chalk");
const yargs = require("yargs");

console.log(chalk.red("Welcome To My Note-app where you can:"));
console.log(chalk.green("Add a new Note Using 'add' command.  "));
console.log(chalk.green("Remove a Note Using 'remove' command."));
console.log(chalk.green("Read a Note Using 'read' command.    "));
console.log(chalk.green("List all Notes Using 'list' command. "));

yargs.command({
    command: "add",
    description: "Add a new note",
    builder: {
        title: {
            describe: "The title of the note",
            demandOption: true,
            type: "string",
        },
        body: {
            describe: "The body of note!",
            demandOption: true,
            type: "string",
        },
    },
    handler(argv) {
        notes.addNote(argv.title, argv.body);
    },
});

yargs.command({
    command: "remove",
    description: "Remove a note",
    builder: {
        title: {
            describe: "The title of the note",
            demandOption: true,
            type: "string",
        },
    },
    handler(argv) {
        notes.removeNotes(argv.title);
    },
});

yargs.command({
    command: "list",
    description: "List all notes",
    handler() {
        notes.listNotes();
    },
});

yargs.command({
    command: "read",
    description: "Read a note",
    builder: {
        title: {
            description: "Title of Note!",
            demandOption: true,
            type: "string",
        },
    },
    handler(argv) {
        notes.readNote(argv.title);
    },
});

yargs.parse();
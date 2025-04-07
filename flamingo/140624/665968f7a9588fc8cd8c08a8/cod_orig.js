function Message(id, text, author, parentId) {
  this.id = id;
  this.text = text;
  this.edited = false;
  this.references = [];
  this.author = author;
  this.timestamp = Date.now();
  this.parentId = parentId; 
}

function ChatArchive() {
  this.messages = [];
  this.rootMessages = []; 
}

ChatArchive.prototype.addMessage = function(message) {
  if (!message.text) {
    console.error("Error: Message cannot have empty text.");
    return;
  }

  if (message.parentId && this.getMessage(message.parentId) === null) {
    console.error("Error: Parent message with ID", message.parentId, "not found.");
    return;
  }

  const newMessage = Object.assign({}, message);
  this.messages.push(newMessage);

  if (!message.parentId) {
    this.rootMessages.push(newMessage); 
  }
};

ChatArchive.prototype.getMessage = function(id) {
  const messageIndex = this.messages.findIndex(m => m.id === id);
  if (messageIndex !== -1) {
    return this.messages[messageIndex];
  } else {
    return null;
  }
};

ChatArchive.prototype._getReplies = function(messageId, thread) {
  for (const message of this.messages) {
    if (message.parentId === messageId) {
      thread.push(message);
      this._getReplies(message.id, thread);
    }
  }
};

ChatArchive.prototype.editMessage = function(id, newText) {
  for (const message of this.messages) { // Mistakenly looping through all messages
    if (message.id === id) {
      message.text = newText;
      message.edited = true;
      break; // Exit the loop after updating the target message
    }
  }
};

const chatArchive = new ChatArchive();
chatArchive.addMessage(new Message(1, "Message 1", "User A", null)); 
chatArchive.addMessage(new Message(2, "Replying to Message 1", "User B", 1));
chatArchive.addMessage(new Message(3, "Re: Replying to Message 1", "User A", 2)); 

chatArchive.addMessage(new Message(4, "Circular reference test", "User B", 1)); 
chatArchive.editMessage(1, "Edited Message 1 (circular reference?)");

const thread = chatArchive.getThread(1);
console.log(thread); 

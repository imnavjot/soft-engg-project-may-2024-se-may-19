<template>
  <div>
    <!-- Sticky search icon button -->
    <button class="search-button" @click="toggleChat">
      <i class="fas fa-search"></i>
    </button>

    <!-- Chat popup -->
    <transition name="fade">
      <div v-if="showChat" class="chat-popup">
        <div class="chat-header">
          <h5>Chat with AI Assistant</h5>
          <button class="close-btn" @click="closeChat">
            <i class="fas fa-times"></i>
          </button>
        </div>
        <div class="chat-body" ref="chatBody">
          <div v-for="(message, index) in messages" :key="index" :class="['chat-message', message.isUser ? 'user-message' : 'ai-message']">
            <div class="message-content">{{ message.text }}</div>
          </div>
        </div>
        <div class="chat-footer">
          <input v-model="userInput" @keyup.enter="sendMessage" placeholder="Type your message..." />
          <button @click="sendMessage">Send</button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showChat: false,
      userInput: '',
      messages: [],
    };
  },
  methods: {
    toggleChat() {
      this.showChat = !this.showChat;
      if (this.showChat) {
        this.clearChat();
        this.$nextTick(() => {
          this.scrollToBottom();
        });
      }
    },
    async sendMessage() {
      if (this.userInput.trim()) {
        this.messages.push({ text: this.userInput, isUser: true });
        const message = this.userInput;
        this.userInput = '';
        await this.fetchAIResponse(message);
        this.scrollToBottom();
      }
    },
    async fetchAIResponse(prompt) {
      try {
        const response = await fetch('http://127.0.0.1:5000/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt }),
        });
        const data = await response.json();
        this.messages.push({ text: data.chat, isUser: false });
      } catch (error) {
        console.error('Error fetching AI response:', error);
      }
    },
    closeChat() {
      this.showChat = false;
      this.clearChat();
    },
    clearChat() {
      this.messages = [];
    },
    scrollToBottom() {
      this.$nextTick(() => {
        const chatBody = this.$refs.chatBody;
        chatBody.scrollTop = chatBody.scrollHeight;
      });
    },
  },
};
</script>

<style scoped>
.search-button {
  position: fixed;
  bottom: 25px;
  right: 25px;
  padding: 10px 14px;
  background-color: #f0f0f0;
  color: #007bff;
  border: none;
  border-radius: 60%;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.search-button:hover {
  background-color: #e0e0e0;
  transform: scale(1.1);
}

.chat-popup {
  position: fixed;
  bottom: 25px; /* Adjusted for better visibility */
  right: 25px;
  width: 350px;
  height: 400px; /* Default height when the chat is first opened */
  max-height: 80vh; /* Maximum height as a percentage of viewport height */
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  z-index: 1000;
}

.chat-header {
  background-color: #f1f1f1;
  border-bottom: 1px solid #ddd;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.chat-header h5 {
  margin: 0;
  font-size: 16px;
  color: #333;
}

.close-btn {
  background: none;
  border: none;
  color: #333;
  font-size: 18px;
  cursor: pointer;
  transition: color 0.3s;
}

.close-btn:hover {
  color: #ff0000;
}

.chat-body {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
  background-color: #f9f9f9;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.chat-message {
  padding: 10px;
  border-radius: 8px;
  max-width: 80%;
  line-height: 1.5;
}

.user-message {
  background-color: #007bff;
  color: #fff;
  align-self: flex-end;
}

.ai-message {
  background-color: #e0e0e0;
  color: #333;
  align-self: flex-start;
}

.chat-footer {
  display: flex;
  padding: 10px;
  border-top: 1px solid #ddd;
  background-color: #f1f1f1;
}

.chat-footer input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 14px;
}

.chat-footer button {
  margin-left: 10px;
  padding: 8px 12px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s;
}

.chat-footer button:hover {
  background-color: #0056b3;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>

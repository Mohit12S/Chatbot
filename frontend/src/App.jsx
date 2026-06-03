import React, { useState, useEffect, useRef } from 'react';
import MessageList from './components/MessageList';
import MessageInput from './components/MessageInput';
import { ChatService } from './services/chatService';

function App() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const messagesEndRef = useRef(null);

  const chatService = new ChatService();

  // Auto-scroll to latest message
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Handle sending a message
  const handleSendMessage = async (messageText) => {
    // Clear any previous errors
    setError('');

    // Add user message to chat
    const userMessage = {
      id: Date.now(),
      text: messageText,
      sender: 'user',
      timestamp: new Date().toLocaleTimeString(),
    };
    setMessages((prev) => [...prev, userMessage]);

    // Show loading state
    setLoading(true);

    try {
      // Call backend API
      const response = await chatService.sendMessage(messageText);

      // Add AI response to chat
      const botMessage = {
        id: Date.now() + 1,
        text: response,
        sender: 'bot',
        timestamp: new Date().toLocaleTimeString(),
      };
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      // Show error message
      const errorMessage = {
        id: Date.now() + 1,
        text: `Error: ${err.message || 'Failed to get response. Please try again.'}`,
        sender: 'error',
        timestamp: new Date().toLocaleTimeString(),
      };
      setMessages((prev) => [...prev, errorMessage]);
      setError(err.message || 'An error occurred. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white border-b border-gray-200 shadow-sm">
        <div className="max-w-2xl mx-auto px-4 py-4">
          <h1 className="text-2xl font-bold text-gray-800">AI Chatbot</h1>
          <p className="text-sm text-gray-500">Ask me anything!</p>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Messages */}
        <div className="flex-1 overflow-y-auto">
          <div className="max-w-2xl mx-auto px-4 py-6">
            {messages.length === 0 ? (
              <div className="flex items-center justify-center h-full text-center">
                <div className="text-gray-400">
                  <p className="text-lg font-semibold mb-2">Welcome to the Chatbot!</p>
                  <p className="text-sm">Start a conversation by sending a message.</p>
                </div>
              </div>
            ) : (
              <>
                <MessageList messages={messages} />
                <div ref={messagesEndRef} />
              </>
            )}
          </div>
        </div>

        {/* Error Message */}
        {error && (
          <div className="bg-red-50 border-b border-red-200">
            <div className="max-w-2xl mx-auto px-4 py-3">
              <p className="text-sm text-red-600">{error}</p>
            </div>
          </div>
        )}

        {/* Input Area */}
        <div className="bg-white border-t border-gray-200">
          <div className="max-w-2xl mx-auto px-4 py-4">
            <MessageInput
              onSendMessage={handleSendMessage}
              loading={loading}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

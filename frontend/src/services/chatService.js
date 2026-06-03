/**
 * Chat Service
 * Handles communication with the backend API
 */

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export class ChatService {
  /**
   * Send a message to the chat API
   * @param {string} message - The user's message
   * @returns {Promise<string>} The AI response
   */
  async sendMessage(message) {
    try {
      const response = await fetch(`${API_BASE_URL}/api/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      });

      if (!response.ok) {
        const error = await response.json().catch(() => ({
          detail: 'Unknown error',
        }));
        throw new Error(error.detail || `HTTP ${response.status}`);
      }

      const data = await response.json();
      return data.answer;
    } catch (error) {
      console.error('Error sending message:', error);
      throw error;
    }
  }

  /**
   * Check API health
   * @returns {Promise<boolean>} True if API is healthy
   */
  async checkHealth() {
    try {
      const response = await fetch(`${API_BASE_URL}/api/health`);
      return response.ok;
    } catch {
      return false;
    }
  }
}

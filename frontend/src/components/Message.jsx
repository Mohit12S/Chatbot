import React from 'react';

function Message({ message }) {
  const isUser = message.sender === 'user';
  const isError = message.sender === 'error';

  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`max-w-xs lg:max-w-md px-4 py-3 rounded-lg ${
          isError
            ? 'bg-red-100 text-red-800 border border-red-300'
            : isUser
            ? 'bg-blue-500 text-white'
            : 'bg-gray-200 text-gray-800'
        }`}
      >
        <p className="text-sm break-words">{message.text}</p>
        <p className={`text-xs mt-1 ${isUser ? 'text-blue-100' : 'text-gray-500'}`}>
          {message.timestamp}
        </p>
      </div>
    </div>
  );
}

export default Message;

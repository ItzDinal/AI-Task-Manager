// Typing indicator placeholder for future streaming AI responses.
function AITypingIndicator() {
  return (
    <div className="flex items-center gap-2 text-xs text-gray-400">
      <span>AI is preparing your suggestions</span>
      <span className="inline-flex gap-1">
        <span className="h-1.5 w-1.5 rounded-full bg-gray-400 animate-ai-dot-1 motion-reduce:animate-none" />
        <span className="h-1.5 w-1.5 rounded-full bg-gray-400 animate-ai-dot-2 motion-reduce:animate-none" />
        <span className="h-1.5 w-1.5 rounded-full bg-gray-400 animate-ai-dot-3 motion-reduce:animate-none" />
      </span>
    </div>
  );
}

export default AITypingIndicator;



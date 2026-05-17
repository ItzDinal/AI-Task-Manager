import { Brain, Sparkles } from "lucide-react";
import AIStatusIndicator from "./AIStatusIndicator.jsx";

// Header for AI assistant card with identity and status.
function AIHeader() {
  return (
    <div className="flex items-center justify-between gap-3">
      <div className="flex items-center gap-2">
        <div className="rounded-xl bg-gray-100 p-2 text-gray-700">
          <Brain size={16} />
        </div>
        <div>
          <h3 className="text-base font-semibold text-gray-900">AI Assistant</h3>
          <p className="text-xs text-gray-500">Good morning, Dinal 👋</p>
        </div>
      </div>
      <div className="flex items-center gap-1 text-gray-500">
        <Sparkles size={14} />
        <AIStatusIndicator />
      </div>
    </div>
  );
}

export default AIHeader;

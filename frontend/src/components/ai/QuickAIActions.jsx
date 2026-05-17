import { Sparkles, Wand2, Zap } from "lucide-react";

const actions = [
  { label: "Generate Plan", icon: Wand2 },
  { label: "Smart Prioritize", icon: Zap },
  { label: "AI Insights", icon: Sparkles },
  { label: "Focus Mode", icon: Wand2 },
];

// Quick AI action buttons (UI-only placeholders).
function QuickAIActions() {
  return (
    <section className="space-y-2">
      <p className="text-xs uppercase tracking-wide text-gray-400">Quick AI Actions</p>
      <div className="grid grid-cols-2 gap-3">
        {actions.map((action) => {
          const Icon = action.icon;
          return (
            <button
              key={action.label}
              type="button"
              className="inline-flex items-center justify-center gap-2 rounded-xl border border-gray-200 bg-white px-4 py-3 text-xs font-medium text-gray-700 transition-all duration-200 hover:bg-gray-100"
            >
              <Icon size={14} />
              <span>{action.label}</span>
            </button>
          );
        })}
      </div>
    </section>
  );
}

export default QuickAIActions;

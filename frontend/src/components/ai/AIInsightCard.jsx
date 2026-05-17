import { Lightbulb } from "lucide-react";

// Highlighted AI productivity insight with supportive guidance.
function AIInsightCard() {
  return (
    <section className="rounded-2xl bg-gradient-to-br from-black to-gray-800 p-5 text-white">
      <div className="flex items-start gap-2">
        <Lightbulb size={16} className="mt-0.5" />
        <div>
          <p className="text-xs uppercase tracking-wide text-gray-300">Smart Insight</p>
          <p className="mt-2 text-sm leading-6 text-gray-100">
            You complete 32% more tasks in the morning. Consider scheduling deep work before 12 PM.
          </p>
        </div>
      </div>
    </section>
  );
}

export default AIInsightCard;

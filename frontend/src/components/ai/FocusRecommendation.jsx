import { Timer } from "lucide-react";

// Focus recommendation card with compact CTA.
function FocusRecommendation() {
  return (
    <section className="rounded-xl border border-gray-200 bg-gray-50 p-4">
      <p className="text-xs uppercase tracking-wide text-gray-400">Recommended Focus Session</p>
      <div className="mt-2 flex items-center justify-between gap-3">
        <div className="min-w-0">
          <p className="text-sm font-medium text-gray-900">Focus on 1 high-priority task for the next 45 minutes.</p>
          <p className="mt-1 text-xs text-gray-500">Duration: 45 Minutes</p>
        </div>
        <div className="rounded-lg bg-white p-2 text-gray-600">
          <Timer size={16} />
        </div>
      </div>
      <button type="button" className="mt-3 rounded-xl border border-gray-200 bg-white px-4 py-2 text-sm font-medium text-gray-700 transition-all duration-200 hover:bg-gray-100">
        Start Focus
      </button>
    </section>
  );
}

export default FocusRecommendation;

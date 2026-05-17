import { Sparkles } from "lucide-react";

// Upgrade card promoting AI features.
function UpgradeCard() {
  return (
    <section className="rounded-2xl border border-gray-200 bg-gray-50 p-4">
      <div className="flex items-start gap-3">
        <div className="mt-0.5 flex h-8 w-8 items-center justify-center rounded-lg bg-black text-white">
          <Sparkles size={14} />
        </div>
        <div className="space-y-2">
          <p className="text-sm font-semibold text-gray-900">Unlock AI Pro</p>
          <p className="text-xs leading-5 text-gray-500">Smart planning and focus recommendations for ADHD-friendly workflows.</p>
          <button
            type="button"
            className="rounded-xl bg-black px-3 py-2 text-xs font-medium text-white transition-all duration-200 hover:bg-gray-800"
          >
            Upgrade
          </button>
        </div>
      </div>
    </section>
  );
}

export default UpgradeCard;

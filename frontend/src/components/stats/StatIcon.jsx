// Icon container for stat cards with neutral and semantic tones.
function StatIcon({ icon: Icon, tone = "neutral" }) {
  const toneClass = {
    positive: "bg-emerald-50 text-emerald-700",
    warning: "bg-amber-50 text-amber-700",
    neutral: "bg-gray-100 text-gray-600",
  }[tone] || "bg-gray-100 text-gray-600";

  return (
    <div className={`inline-flex rounded-xl p-3 ${toneClass}`}>
      <Icon size={18} />
    </div>
  );
}

export default StatIcon;

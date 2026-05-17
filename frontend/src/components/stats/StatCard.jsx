import StatIcon from "./StatIcon.jsx";
import StatTrend from "./StatTrend.jsx";

// Reusable metric card for dashboard productivity insights.
function StatCard({ icon, tone, title, value, trend, trendText, subtitle }) {
  return (
    <article className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm transition-all duration-200 hover:shadow-md">
      <div className="flex items-start justify-between gap-3">
        <StatIcon icon={icon} tone={tone} />
        <StatTrend trend={trend} text={trendText} />
      </div>

      <div className="mt-5 space-y-1">
        <p className="text-sm text-gray-500">{title}</p>
        <p className="text-3xl font-bold text-gray-900">{value}</p>
        <p className="text-sm text-gray-400">{subtitle}</p>
      </div>
    </article>
  );
}

export default StatCard;

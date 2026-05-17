import { Minus, TrendingDown, TrendingUp } from "lucide-react";

// Small trend indicator for period-over-period stat movement.
function StatTrend({ trend = "neutral", text }) {
  const config = {
    positive: { icon: TrendingUp, className: "text-emerald-700" },
    warning: { icon: TrendingDown, className: "text-amber-700" },
    neutral: { icon: Minus, className: "text-gray-500" },
  }[trend] || { icon: Minus, className: "text-gray-500" };

  const TrendIcon = config.icon;

  return (
    <div className={`inline-flex items-center gap-1 text-xs font-medium ${config.className}`}>
      <TrendIcon size={14} />
      <span>{text}</span>
    </div>
  );
}

export default StatTrend;

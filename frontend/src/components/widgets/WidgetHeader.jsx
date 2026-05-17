// Reusable widget heading with optional action button.
function WidgetHeader({ title, actionLabel = "View All" }) {
  return (
    <div className="flex items-center justify-between gap-3">
      <h3 className="text-base font-semibold text-gray-900">{title}</h3>
      <button
        type="button"
        className="text-xs font-medium text-gray-500 transition-all duration-200 hover:text-gray-700"
      >
        {actionLabel} →
      </button>
    </div>
  );
}

export default WidgetHeader;
